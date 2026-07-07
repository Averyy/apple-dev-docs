# element::ageOverLifetime

**Framework**: Compute Graph  
**Kind**: func

Returns the normalized age of the element as a ratio of its lifetime.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
float element::ageOverLifetime()
```

#### Return Value

A normalized value representing age divided by lifetime

#### Discussion

Use this function to get a value between 0.0 (just created) and 1.0 (end of life), which is ideal for interpolating properties over the element’s lifetime.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/3e911934fec89dca62b330fb3faa729a/element__ageOverLifetime.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/element/ageoverlifetime)*