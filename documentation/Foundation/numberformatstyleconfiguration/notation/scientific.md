# scientific

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A notation constant that formats values with scientific notation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var scientific: NumberFormatStyleConfiguration.Notation { get }
```

#### Discussion

The following example shows the effect of using scientific notation with a format style:

```swift
let scientific = 12345.formatted(.number
    .notation(.scientific)) // 1.2345E4"

```

## See Also

### Notations
- [static var automatic: NumberFormatStyleConfiguration.Notation](./automatic.md)
  A notation that automatically provides locale-appropriate behavior.
- [static var compactName: NumberFormatStyleConfiguration.Notation](./compactname.md)
  A locale-appropriate compact name notation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/notation/scientific)*