# predictions(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Classifies a data column with labels.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 13.0
- visionOS 1.0+

> **Deprecated**: Use DataFrame instead of MLDataTable.

## Declaration

```swift
func predictions(from texts: MLDataColumn<String>) throws -> MLDataColumn<String>
```

**Other overloads**:

```swift
func predictions(from texts: [String]) throws -> [String]
```

## Return Value

An array of labels for the given strings.

## Parameters

- `texts`: The data column of strings to be classified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/predictions(from:)-40gtb)*