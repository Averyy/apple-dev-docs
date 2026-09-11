# makeCase(_:)

**Framework**: App Intents Testing  
**Kind**: method

Creates an enumeration case with the specified raw value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

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