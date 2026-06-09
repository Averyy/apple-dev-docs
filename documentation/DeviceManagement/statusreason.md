# StatusReason

**Framework**: Device Management  
**Kind**: dictionary

Provides details about an error for an item in a status report.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object StatusReason
```

#### Discussion

Each status item defines its own set of `code`, `description`, and `details` values.

##### Status Item Example

```json
{
    "code": "Error.InstallFailed",
    "description": "The app installation failed.",
    "details": {
        "Timestamp": "2025-05-15T10:30:00Z"
    }
}
```

## Topics

### Dictionaries
- [object StatusReason.ErrorDetails](statusreason/errordetails.md)

## Properties

- `Code` (string) *(required)*
- `Description` (string)
- `Details` (StatusReason.ErrorDetails)

## See Also

- [object StatusReport](statusreport.md)
  Provides details about an error for an item in a status report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusreason)*