# init(labeledBySubdirectoryNamesAt:type:continueOnFailure:)

**Framework**: Create ML Components  
**Kind**: init  
**Role**: Initializer

Reads training examples from a directory containing files in labeled sub-directories.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
init(labeledBySubdirectoryNamesAt url: URL, type: UTType, continueOnFailure: Bool = false) throws
```

## Discussion

Take for example this directory structure:

```
/
    foo/
        file1.png
        file2.png
    bar/
        file3.png
        file4.png
```

It would produce two labels (foo and bar) with two URLs each.

## Parameters

- `url`: URL of directory containing the files.
- `type`: Type of files.
- `continueOnFailure`: A Boolean value indicating whether to continue reading files after encountering a file that is not readable. The default value is `false`.

## See Also

### Creating the feature
- [init(labeledByNamesAt: URL, separator: Character, index: Int, type: UTType, continueOnFailure: Bool) throws](./init%28labeledbynamesat,separator,index,type,continueonfailure%29.md)
  Reads training examples from a directory containing files having their labels in the name. The name can contain multiple words separated by a `separator`. So the `index` tells the position of the label in the file name. Files with incorrect name format are ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedfiles/init(labeledbysubdirectorynamesat:type:continueonfailure:))*