# compileModel(at:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Type Method

Compile a model for a device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class func compileModel(at url: URL) async throws -> URL
```

**Other overloads**:

```swift
class func compileModel(at modelURL: URL) async throws -> URL
```

```swift
class func compileModel(at modelURL: URL) throws -> URL
```

## Mentions

- [Analyzing a Core ML model’s performance in Xcode](../analyzing-a-core-ml-model-s-performance-in-xcode.md)

## Return Value

A URL to the compiled model directory, if successful; otherwise, `nil`.

## Parameters

- `url`: The URL to the model file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/compilemodel(at:)-45ao6)*