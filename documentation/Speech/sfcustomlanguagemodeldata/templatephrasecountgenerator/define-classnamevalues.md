# define(className:values:)

**Framework**: Speech  
**Kind**: method

Define a class of tokens to be used in template strings.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
func define(className: String, values: [String])
```

## Parameters

- `className`: A string which will appear in template strings inside of angle brackets.
- `values`: The set of values which may be substituted into the template strings.

## See Also

- [func hash(into: inout Hasher)](sfcustomlanguagemodeldata/templatephrasecountgenerator/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [func insert(template: String, count: Int)](sfcustomlanguagemodeldata/templatephrasecountgenerator/insert(template:count:).md)
  Add a template to be used to generate data samples.
- [func makeAsyncIterator() -> SFCustomLanguageModelData.PhraseCountGenerator.Iterator](sfcustomlanguagemodeldata/templatephrasecountgenerator/makeasynciterator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/templatephrasecountgenerator/define(classname:values:))*