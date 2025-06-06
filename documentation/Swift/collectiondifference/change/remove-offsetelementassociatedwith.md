# CollectionDifference.Change.remove(offset:element:associatedWith:)

**Framework**: Swift  
**Kind**: case

A removal.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case remove(offset: Int, element: ChangeElement, associatedWith: Int?)
```

#### Discussion

The `offset` value is the offset of the element to be removed in the original state of the collection. A non-`nil` `associatedWith` value is the offset of the complementary change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectiondifference/change/remove(offset:element:associatedwith:))*