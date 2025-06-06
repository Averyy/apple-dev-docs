# init(coreMLPackageAtURL:descriptor:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Initialize the executable with the Core ML model package at the provided URL.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
init(coreMLPackageAtURL coreMLPackageURL: URL, descriptor compilationDescriptor: MPSGraphCompilationDescriptor?)
```

## Parameters

- `coreMLPackageURL`: The URL where to read the Core ML model package.
- `compilationDescriptor`: Compilation descriptor to be used to specialize, since the executable was created with a compilationDescriptor already this one overrides those settings to the extent it can.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutable/init(coremlpackageaturl:descriptor:))*