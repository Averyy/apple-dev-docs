# starts(with:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in the specified regex.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func starts(with regex: some RegexComponent) -> Bool
```

#### Return Value

`true` if the initial elements of the sequence matches the beginning of `regex`; otherwise, `false`.

## Parameters

- `regex`: A regex to compare to this sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bidirectionalcollection/starts(with:)-4972u)*