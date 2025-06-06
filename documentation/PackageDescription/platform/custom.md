# custom(_:)

**Framework**: PackageDescription  
**Kind**: method

Creates a custom platform.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
static func custom(_ platformName: String) -> Platform
```

#### Return Value

A `Platform` instance.

#### Discussion

Use this function if none of the predefined platform names match the platform you are targeting.

## Parameters

- `platformName`: The name of the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/platform/custom(_:))*