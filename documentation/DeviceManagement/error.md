# Error

**Framework**: Device Management  
**Kind**: dictionary

Information about an error that occurred while processing a request.

**Availability**:
- VPP License Management 2.1+

## Declaration

```swift
object Error
```

## Topics

### Related Objects
- [object Error.Source](error/source-data.dictionary.md)
  An object that represents the source of an error.

## Properties

- `code` (string) *(required)*: The specific code for the underlying cause of the error.
- `detail` (string): More detailed information about the cause of the error, intended to help identify possible resolutions.
- `id` (string) *(required)*: The identifier of the error, mapping to the occurrence.
- `source` (Error.Source): An object containing a reference to the source of the error.
- `status` (string) *(required)*: The HTTP status code the error maps to.
- `title` (string) *(required)*: A developer-friendly title for the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/error)*