# object(forInfoDictionaryKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the value associated with the specified key in the receiver’s information property list.

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
func object(forInfoDictionaryKey key: String) -> Any?
```

```objc
- (id) objectForInfoDictionaryKey:(NSString *) key;
```

## Return Value

The value associated with `key` in the receiver’s property list (`Info.plist`). The localized value of a key is returned when one is available.

## Discussion

Use of this method is preferred over other access methods because it returns the localized value of a key when one is available.

## Parameters

- `key`: A key in the receiver’s property list.

## See Also

### Getting bundle information
- [var bundleURL: URL](./bundleurl.md)
  The full URL of the receiver’s bundle directory.
- [var bundlePath: String](./bundlepath.md)
  The full pathname of the receiver’s bundle directory.
- [var bundleIdentifier: String?](./bundleidentifier.md)
  The receiver’s bundle identifier.
- [var infoDictionary: [String : Any]?](./infodictionary.md)
  A dictionary, constructed from the bundle’s `Info.plist` file, that contains information about the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/object(forinfodictionarykey:))*