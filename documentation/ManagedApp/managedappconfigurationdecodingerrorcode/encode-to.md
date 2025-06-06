# encode(to:)

**Framework**: ManagedApp  
**Kind**: method

Encodes this value into the given encoder, when the type’s `RawValue` is `Int`.

**Availability**:
- iOS ?+
- iPadOS ?+
- visionOS ?+

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

#### Discussion

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/managedappconfigurationdecodingerrorcode/encode(to:))*