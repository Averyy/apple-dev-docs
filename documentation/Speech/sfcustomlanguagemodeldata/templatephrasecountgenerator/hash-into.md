# hash(into:)

**Framework**: Speech  
**Kind**: method

Hashes the essential components of this value by feeding them into the given hasher.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
override func hash(into hasher: inout Hasher)
```

#### Discussion

Implement this method to conform to the `Hashable` protocol. The components used for hashing must be the same as the components compared in your type’s `==` operator implementation. Call `hasher.combine(_:)` with each of these components.

> ❗ **Important**: In your implementation of `hash(into:)`, don’t call `finalize()` on the `hasher` instance provided, or replace it with a different instance. Doing so may become a compile-time error in the future.

## Parameters

- `hasher`: The hasher to use when combining the components   of this instance.

## See Also

- [func define(className: String, values: [String])](sfcustomlanguagemodeldata/templatephrasecountgenerator/define(classname:values:).md)
  Define a class of tokens to be used in template strings.
- [func insert(template: String, count: Int)](sfcustomlanguagemodeldata/templatephrasecountgenerator/insert(template:count:).md)
  Add a template to be used to generate data samples.
- [func makeAsyncIterator() -> SFCustomLanguageModelData.PhraseCountGenerator.Iterator](sfcustomlanguagemodeldata/templatephrasecountgenerator/makeasynciterator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/templatephrasecountgenerator/hash(into:))*