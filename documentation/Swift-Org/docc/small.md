---
url: "https://docs.swift.org/latest/documentation/docc/small"
framework: "Swift-Org/docc"
---

# Small

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A directive for specifying small print text like legal, license, or copyright text that should be rendered in a smaller font size.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@Small {
    ...
}
```

#### Overview

The `@Small` directive is based on HTML’s small tag (`<small>`). It supports any inline markup formatting like bold and italics but does not support more structured markup like [`Row`](./row.md) and `Row/Column`.

```md
You can create a sloth using the ``init(name:color:power:)``
initializer, or create randomly generated sloth using a
``SlothGenerator``:
   
   let slothGenerator = MySlothGenerator(seed: randomSeed())
   let habitat = Habitat(isHumid: false, isWarm: true)

   // ...

@Small {
    _Licensed under Apache License v2.0 with Runtime Library Exception._
}
```

## See Also

### Creating Custom Page Layouts
- [@Row(numberOfColumns: Int)](./row.md)
  A container directive that arranges content into a grid-based row and column layout.
- [@TabNavigator](./tabnavigator.md)
  A container directive that arranges content into a tab-based layout.
- [@Links(visualStyle: VisualStyle)](./links.md)
  A directive for authoring authoring embedded previews of documentation links (similar to how links are currently rendered in Topics sections) anywhere on the page without affecting page curation behavior.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/small)*