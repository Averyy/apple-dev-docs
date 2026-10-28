---
url: "https://swiftpackageindex.com/apple/swift-openapi-generator/main/documentation/swift_openapi_generator/handlefileoperation(at:filedescription:operation:)"
framework: "swift-openapi-generator/swift_openapi_generator"
---

# handleFileOperation(at:fileDescription:operation:)

**Framework**: swift-openapi-generator/swift_openapi_generator  
**Kind**: func  
**Role**: Function

Executes a throwing operation and transforms file-not-found errors into user-friendly messages.

## Declaration

```swift
func handleFileOperation<T>(at url: URL, fileDescription: String = "Configuration file", operation: () throws -> T) throws -> T
```

## Return Value

The result of the operation.

## Discussion

> **Throws**: A `ValidationError` with a user-friendly message if the file is not found, or the original error wrapped in a `ValidationError` for other errors.

## Parameters

- `url`: The file URL that the operation is attempting to access.
- `fileDescription`: A description of the file type (e.g., “Configuration file”, “OpenAPI document”).
- `operation`: The throwing operation to execute.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-openapi-generator/main/documentation/swift_openapi_generator/handlefileoperation(at:filedescription:operation:))*