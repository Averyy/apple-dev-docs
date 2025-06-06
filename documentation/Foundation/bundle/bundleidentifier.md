# bundleIdentifier

**Framework**: Foundation  
**Kind**: property

The receiver’s bundle identifier.

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
var bundleIdentifier: String? { get }
```

#### Discussion

The bundle identifier is defined by the `CFBundleIdentifier` key in the bundle’s information property list.

## See Also

- [var bundleURL: URL](bundle/bundleurl.md)
  The full URL of the receiver’s bundle directory.
- [var bundlePath: String](bundle/bundlepath.md)
  The full pathname of the receiver’s bundle directory.
- [var infoDictionary: [String : Any]?](bundle/infodictionary.md)
  A dictionary, constructed from the bundle’s `Info.plist` file, that contains information about the receiver.
- [func object(forInfoDictionaryKey: String) -> Any?](bundle/object(forinfodictionarykey:).md)
  Returns the value associated with the specified key in the receiver’s information property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/bundleidentifier)*