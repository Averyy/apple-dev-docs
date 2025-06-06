# unkeyedContainer()

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Returns an encoding container appropriate for holding multiple unkeyed values.

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
func unkeyedContainer() -> any UnkeyedEncodingContainer
```

#### Return Value

A new empty unkeyed container.

#### Discussion

You must use only one kind of top-level encoding container. This method must not be called after a call to `container(keyedBy:)` or after encoding a value through a call to `singleValueContainer()`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/encoder/unkeyedcontainer())*