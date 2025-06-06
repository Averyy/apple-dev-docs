# conformsTo

**Framework**: HIDDriverKit  
**Kind**: method

**Availability**:
- DriverKit 21.0+
- macOS ?+

## Declaration

```swift
bool conformsTo(uint32_t usagePage, uint32_t usage);
```

#### Return Value

Returns a bool specifying if the element conforms to the provided usage page and usage.

#### Discussion

Checks if the element conforms to the provided usage page and usage somewhere in its hierarchy.

## Parameters

- `usagePage`: The usage page to check for conformity.
- `usage`: The usage to check for conformity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelement/conformsto)*