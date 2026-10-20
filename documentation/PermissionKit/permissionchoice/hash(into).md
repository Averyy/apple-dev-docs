# hash(into:)

**Framework**: PermissionKit  
**Kind**: method  
**Role**: Instance Method

Performs a hash operation on the value by feeding its hash values into the given hasher.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher`: The hasher to use when combining the values of this instance.

## See Also

### Computing hashes
- [static func == (PermissionChoice, PermissionChoice) -> Bool](./eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionchoice/hash(into:))*