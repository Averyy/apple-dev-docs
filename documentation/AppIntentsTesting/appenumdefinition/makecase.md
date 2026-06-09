# makeCase(_:)

**Framework**: App Intents Testing  
**Kind**: method

Creates an enumeration case with the specified raw value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func makeCase(_ rawValue: String) -> AnyAppEnum
```

## Mentions

- [Testing your App Intents code](testing-your-app-intents-code.md)

#### Return Value

A type-erased enumeration instance with the specified value.

#### Discussion

The provided `rawValue` needs to match one of your enum’s cases.

## Parameters

- `rawValue`: The string representation of the enumeration case.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appenumdefinition/makecase(_:))*