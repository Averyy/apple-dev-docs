# shouldArchiveValue(forKey:)

**Framework**: Core Animation  
**Kind**: method

Specifies whether the value of the property for a given key is archived.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func shouldArchiveValue(forKey key: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the specified property should be archived, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Called by the object’s implementation of `encodeWithCoder:`. The object must implement keyed archiving.

The default implementation returns [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `key`: The name of one of the receiver’s properties.

## See Also

- [Core Animation Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimation/shouldarchivevalue(forkey:))*