# unmountAndEjectDevice(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attempts to eject the volume mounted at the given path.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func unmountAndEjectDevice(at url: URL) throws
```

```objc
- (BOOL) unmountAndEjectDeviceAtURL:(NSURL *) url error:(NSError **) error;
```

## Discussion

You can safely call this method from any thread of your app.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The URL of the volume to eject.

## See Also

### Unmounting a Device
- [func unmountAndEjectDevice(atPath: String) -> Bool](./unmountandejectdevice%28atpath%29.md)
  Unmounts and ejects the device at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/unmountandejectdevice(at:))*