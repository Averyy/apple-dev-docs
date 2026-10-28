---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.struct/sourcelocation-swift.struct"
framework: "swift-configuration/Configuration"
---

# AccessEvent.Metadata.SourceLocation

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

The source code location where a configuration access occurs.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct SourceLocation
```

## Overview

Captures the file identifier and line number for debugging and auditing purposes.

## Topics

### Creating a source location
- [init(fileID: String, line: UInt)](./sourcelocation-swift.struct/init%28fileid,line%29.md)
  Creates a new source location.
### Inspecting a source location
- [var fileID: String](./sourcelocation-swift.struct/fileid.md)
  The identifier of the source file where the access occurs.
- [var line: UInt](./sourcelocation-swift.struct/line.md)
  The line number within the source file where the access occurs.
- [var description: String](./sourcelocation-swift.struct/description.md)

## Relationships

### Conforms To
- Swift.CustomStringConvertible
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.struct/sourcelocation-swift.struct)*