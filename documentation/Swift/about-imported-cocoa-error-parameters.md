# About Imported Cocoa Error Parameters

**Framework**: Swift

Learn how Cocoa error parameters are converted to Swift throwing methods.

#### Overview

In Cocoa, methods that produce errors take an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) pointer parameter as their last parameter, which populates its argument with an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object if an error occurs. Swift automatically translates Objective-C methods that produce errors into methods that throw an error according to Swift’s native error handling functionality.

##### Understand How Error Parameters Are Imported

Swift examines Objective-C method declarations and translates them into Swift throwing methods, with shorter names when possible.

For example, consider the [`removeItem(at:)`](https://developer.apple.com/documentation/Foundation/FileManager/removeItem(at:)) method from [`FileManager`](https://developer.apple.com/documentation/Foundation/FileManager). In Objective-C, it’s declared like this:

```occ
- (BOOL)removeItemAtURL:(NSURL *)URL
                  error:(NSError **)error;
```

In Swift, it’s imported like this:

```swift
func removeItem(at: URL) throws
```

Notice that the [`removeItem(at:)`](https://developer.apple.com/documentation/Foundation/FileManager/removeItem(at:)) method is imported by Swift with a `Void` return type, no error parameter, and a `throws` declaration.

If the last non-block parameter of an Objective-C method is of type `NSError **`, Swift replaces it with the throws keyword, to indicate that the method can throw an error. If the Objective-C method’s error parameter is also its first parameter, Swift attempts to simplify the method name further, by removing the `WithError` or `AndReturnError` suffix, if present, from the first part of the selector. If another method is declared with the resulting selector, the method name is not changed.

If an error producing Objective-C method returns a [`BOOL`](https://developer.apple.com/documentation/ObjectiveC/BOOL) value to indicate the success or failure of a method call, Swift changes the return type of the function to `Void`. Similarly, if an error producing Objective-C method returns a `nil` value to indicate the failure of a method call, Swift changes the return type of the function to a nonoptional type.

Otherwise, if no convention can be inferred, the method is left intact.

> **Note**: You use the `NS_SWIFT_NOTHROW` macro on Objective-C method declarations that produce an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) to prevent it from being imported by Swift as a method that throws.

## See Also

- [Using Key-Value Observing in Swift](using-key-value-observing-in-swift.md)
  Notify objects about changes to the properties of other objects.
- [Using Delegates to Customize Object Behavior](using-delegates-to-customize-object-behavior.md)
  Respond to events on behalf of a delegator.
- [Managing a Shared Resource Using a Singleton](managing-a-shared-resource-using-a-singleton.md)
  Provide access to a shared resource using a single, shared class instance.
- [Handling Cocoa Errors in Swift](handling-cocoa-errors-in-swift.md)
  Throw and catch errors that use Cocoa’s error types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/about-imported-cocoa-error-parameters)*