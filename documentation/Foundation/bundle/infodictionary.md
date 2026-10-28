# infoDictionary

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A dictionary, constructed from the bundle’s `Info.plist` file, that contains information about the receiver.

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
var infoDictionary: [String : Any]? { get }
```

```objc
@property (copy, readonly, nullable) NSDictionary<NSString *,id> * infoDictionary;
```

## Discussion

If the bundle does not contain an `Info.plist` file, this dictionary contains only private keys that are used internally by the [`Bundle`](../bundle.md) class. The [`Bundle`](../bundle.md) class may add extra keys to this dictionary for its own use. Common keys for accessing the values of the dictionary are `CFBundleIdentifier`, `NSMainNibFile`, and `NSPrincipalClass`.

## See Also

### Related Documentation
- [var principalClass: AnyClass?](./principalclass.md)
  The bundle’s principal class.
- [+ dictionaryWithContentsOfFile:](../nsdictionary/dictionarywithcontentsoffile_.md)
  Creates a dictionary using the keys and values found in a file specified by a given path.
### Getting bundle information
- [var bundleURL: URL](./bundleurl.md)
  The full URL of the receiver’s bundle directory.
- [var bundlePath: String](./bundlepath.md)
  The full pathname of the receiver’s bundle directory.
- [var bundleIdentifier: String?](./bundleidentifier.md)
  The receiver’s bundle identifier.
- [func object(forInfoDictionaryKey: String) -> Any?](./object%28forinfodictionarykey%29.md)
  Returns the value associated with the specified key in the receiver’s information property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/infodictionary)*