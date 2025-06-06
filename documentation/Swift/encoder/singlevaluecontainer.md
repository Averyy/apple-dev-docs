# singleValueContainer()

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Returns an encoding container appropriate for holding a single primitive value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func singleValueContainer() -> any SingleValueEncodingContainer
```

#### Return Value

A new empty single value container.

#### Discussion

You must use only one kind of top-level encoding container. This method must not be called after a call to `unkeyedContainer()` or `container(keyedBy:)`, or after encoding a value through a call to `singleValueContainer()`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/encoder/singlevaluecontainer())*