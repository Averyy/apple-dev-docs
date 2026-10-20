# init(file:)

**Framework**: Quartz  
**Kind**: init  
**Role**: Initializer

Returns a composition object initialized with a Quartz Composer composition file.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
init!(file path: String!)
```

```objc
+ (QCComposition *) compositionWithFile:(NSString *) path;
```

#### Return Value

A Quartz Composer composition object or `nil` if there is an error.

## Parameters

- `path`: A path to a file created with the Quartz Composer developer tool (`.qtz` extension).

## See Also

### Creating a Composition
- [init!(data: Data!)](./init%28data%29.md)
  Returns a composition object  initialized with the contents of a Quartz Composer composition file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccomposition/init(file:))*