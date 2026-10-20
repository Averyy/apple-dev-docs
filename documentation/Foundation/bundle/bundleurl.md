# bundleURL

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The full URL of the receiver’s bundle directory.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var bundleURL: URL { get }
```

```objc
@property (copy, readonly) NSURL * bundleURL;
```

## See Also

### Getting bundle information
- [var bundlePath: String](./bundlepath.md)
  The full pathname of the receiver’s bundle directory.
- [var bundleIdentifier: String?](./bundleidentifier.md)
  The receiver’s bundle identifier.
- [var infoDictionary: [String : Any]?](./infodictionary.md)
  A dictionary, constructed from the bundle’s `Info.plist` file, that contains information about the receiver.
- [func object(forInfoDictionaryKey: String) -> Any?](./object%28forinfodictionarykey%29.md)
  Returns the value associated with the specified key in the receiver’s information property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/bundleurl)*