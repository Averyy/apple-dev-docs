# init(clean:reduce:avoid:unknown:)

**Framework**: EnergyKit  
**Kind**: init

Creates an instance of the grid cleanliness data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
init(clean: Measure?, reduce: Measure?, avoid: Measure?, unknown: Measure?)
```

## Parameters

- `clean`: The duration of energy or runtime data during times that were clean.
- `reduce`: The duration of energy or runtime data during times that were reduce periods.
- `avoid`: The duration of energy or runtime data during times to be avoided.
- `unknown`: The unknown duration of energy or runtime data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightrecord/gridcleanliness/init(clean:reduce:avoid:unknown:))*