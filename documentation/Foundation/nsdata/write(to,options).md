# write(to:options:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes the data object’s bytes to the location specified by a given URL.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func write(to url: URL, options writeOptionsMask: NSData.WritingOptions = []) throws
```

```objc
- (BOOL) writeToURL:(NSURL *) url options:(NSDataWritingOptions) writeOptionsMask error:(NSError **) errorPtr;
```

#### Discussion

Since at present only `file://` URLs are supported, there is no difference between this method and [`write(toFile:options:)`](./write%28tofile,options%29.md), except for the type of the first argument.

This method may not be appropriate when writing to publicly accessible files. To securely write data to a public location, use [`FileHandle`](../filehandle.md) instead. For more information, see[Securing File Operations](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585-SW9) in [Secure Coding Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The location to which to write the receiver’s bytes.
- `writeOptionsMask`: A mask that specifies options for writing the data. Constant components are described in [`NSData.WritingOptions`](./writingoptions.md).

## See Also

### Writing Data to a File
- [func write(toFile: String, atomically: Bool) -> Bool](./write%28tofile,atomically%29.md)
  Writes the data object’s bytes to the file specified by a given path.
- [func write(toFile: String, options: NSData.WritingOptions) throws](./write%28tofile,options%29.md)
  Writes the data object’s bytes to the file specified by a given path.
- [func write(to: URL, atomically: Bool) -> Bool](./write%28to,atomically%29.md)
  Writes the data object’s bytes to the location specified by a given URL.
- [NSData.WritingOptions](./writingoptions.md)
  Options for methods used to write data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/write(to:options:))*