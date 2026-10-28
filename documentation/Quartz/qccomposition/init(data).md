# init(data:)

**Framework**: Quartz  
**Kind**: init  
**Role**: Initializer

Returns a composition object  initialized with the contents of a Quartz Composer composition file.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
init!(data: Data!)
```

```objc
+ (QCComposition *) compositionWithData:(NSData *) data;
```

## Return Value

A Quartz Composer composition object or `nil` if there is an error.

## Parameters

- `data`: The contents of a file created with the Quartz Composer developer tool.

## See Also

### Creating a Composition
- [init!(file: String!)](./init%28file%29.md)
  Returns a composition object initialized with a Quartz Composer composition file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccomposition/init(data:))*