# SecKeyCopyAttributes(_:)

**Framework**: Security  
**Kind**: func

Gets the attributes of a given key.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func SecKeyCopyAttributes(_ key: SecKey) -> CFDictionary?
```

#### Return Value

A dictionary containing the key’s attributes. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free this dictionary’s memory when you are done with it.

## Parameters

- `key`: The key whose attributes you want.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeycopyattributes(_:))*