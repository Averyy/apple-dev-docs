# bundlePath

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The full pathname of the receiver’s bundle directory.

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
var bundlePath: String { get }
```

```objc
@property (copy, readonly) NSString * bundlePath;
```

## See Also

### Getting bundle information
- [var bundleURL: URL](./bundleurl.md)
  The full URL of the receiver’s bundle directory.
- [var bundleIdentifier: String?](./bundleidentifier.md)
  The receiver’s bundle identifier.
- [var infoDictionary: [String : Any]?](./infodictionary.md)
  A dictionary, constructed from the bundle’s `Info.plist` file, that contains information about the receiver.
- [func object(forInfoDictionaryKey: String) -> Any?](./object%28forinfodictionarykey%29.md)
  Returns the value associated with the specified key in the receiver’s information property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/bundlepath)*