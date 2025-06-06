# Handling Cocoa Errors in Swift

**Framework**: Swift

Throw and catch errors that use Cocoa’s error types.

#### Overview

You use Swift’s `throw` statement and `do`-`catch` statement to throw and catch errors from Cocoa APIs.  Swift imports Cocoa methods with error parameters as throwing methods, as described in [`About Imported Cocoa Error Parameters`](about-imported-cocoa-error-parameters.md).

##### Catch Errors

In Swift, calling a method that throws requires explicit error handling. Because Cocoa methods with errors parameters are imported as throwing methods, you handle them using Swift’s `do`-`catch` statement.

Here’s an example of how you handle an error when calling a method in Objective-C:

```occ
NSFileManager *fileManager = [NSFileManager defaultManager];
NSURL *fromURL = [NSURL fileURLWithPath:@"/path/to/old"];
NSURL *toURL = [NSURL fileURLWithPath:@"/path/to/new"];
NSError *error = nil;
BOOL success = [fileManager moveItemAtURL:fromURL toURL:toURL error:&error];
if (!success) {
    NSLog(@"Error: %@", error.domain);
}
```

Here’s how you handle the same error in Swift:

```swift
let fileManager = FileManager.default
let fromURL = URL(fileURLWithPath: "/path/to/old")
let toURL = URL(fileURLWithPath: "/path/to/new")
do {
    try fileManager.moveItem(at: fromURL, to: toURL)
} catch let error as NSError {
    print("Error: \(error.domain)")
}
```

You can also use the `do`-`catch` statement to match on specific Cocoa error codes to differentiate possible failure conditions:

```swift
do {
    try fileManager.moveItem(at: fromURL, to: toURL)
} catch CocoaError.fileNoSuchFile {
    print("Error: no such file exists")
} catch CocoaError.fileReadUnsupportedScheme {
    print("Error: unsupported scheme (should be 'file://')")
}
```

##### Throw Errors

You throw Cocoa errors by initializing a Cocoa error type and passing in the relevant error domain and code:

```swift
throw NSError(domain: NSURLErrorDomain, code: NSURLErrorCannotOpenFile, userInfo: nil)
```

If Objective-C code calls a Swift method that throws an error, the error is automatically propagated to the error pointer argument of the bridged Objective-C method.

##### Throw and Catch Errors From Custom Error Domains

You use custom error domains in Cocoa to group related categories of errors. The example below uses the `NS_ERROR_ENUM` macro to group error constants:

```occ
extern NSErrorDomain const MyErrorDomain;
typedef NS_ERROR_ENUM(MyErrorDomain, MyError) {
    specificError1 = 0,
    specificError2 = 1
};
```

This example shows how to throw errors using that custom error type in Swift:

```swift
func customThrow() throws {
    throw NSError(
        domain: MyErrorDomain,
        code: MyError.specificError2.rawValue,
        userInfo: [
            NSLocalizedDescriptionKey: "A customized error from MyErrorDomain."
        ]
    )
}
```

This example shows how to catch errors from a particular error domain and bring attention to unhandled errors from other error domains:

```swift
do {
    try customThrow()
} catch MyError.specificError1 {
    print("Caught specific error #1")
} catch let error as MyError where error.code == .specificError2 {
    print("Caught specific error #2, ", error.localizedDescription)
    // Prints "Caught specific error #2. A customized error from MyErrorDomain."
} catch let error {
    fatalError("Some other error: \(error)")
}
```

##### Handle Exceptions in Objective C Only

In Objective-C, exceptions are distinct from errors. Objective-C exception handling uses the `@try`, `@catch`, and `@throw` syntax to indicate unrecoverable programmer errors. This is distinct from the Cocoa pattern—described above—that uses a trailing [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) parameter to indicate recoverable errors that you plan for during development.

In Swift, you can recover from errors passed using Cocoa’s error pattern, as described above in [`Catch Errors`](handling-cocoa-errors-in-swift#Catch-Errors.md). However, there’s no safe way to recover from Objective-C exceptions in Swift. To handle Objective-C exceptions, write Objective-C code that catches exceptions before they reach any Swift code.

## See Also

- [Using Key-Value Observing in Swift](using-key-value-observing-in-swift.md)
  Notify objects about changes to the properties of other objects.
- [Using Delegates to Customize Object Behavior](using-delegates-to-customize-object-behavior.md)
  Respond to events on behalf of a delegator.
- [Managing a Shared Resource Using a Singleton](managing-a-shared-resource-using-a-singleton.md)
  Provide access to a shared resource using a single, shared class instance.
- [About Imported Cocoa Error Parameters](about-imported-cocoa-error-parameters.md)
  Learn how Cocoa error parameters are converted to Swift throwing methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/handling-cocoa-errors-in-swift)*