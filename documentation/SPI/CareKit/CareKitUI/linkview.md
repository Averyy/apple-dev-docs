---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview"
framework: "CareKit/CareKitUI"
---

# LinkView

**Framework**: CareKit/CareKitUI  
**Kind**: struct  
**Role**: Structure

A card that displays multiple link buttons. Links buttons are capable of showing content in or out of app. Link buttons can be configured using a `Link`.

## Declaration

```swift
@MainActor
struct LinkView<Header> where Header : View
```

## Style

The card supports styling using `careKitStyle(_:)`.

```
    +-------------------------------------------------------+
    |                                                       |
    |  <Title>                                              |
    |  <Detail>                                             |
    |                                                       |
    |  --------------------------------------------------   |
    |                                                       |
    |  <Instructions>                                       |
    |                                                       |
    |  +-------------------------------------------------+  |
    |  | <Link Title>                           <Image>  |  |
    |  +-------------------------------------------------+  |
    |                                                       |
    |  +-------------------------------------------------+  |
    |  | <Link Title>                           <Image>  |  |
    |  +-------------------------------------------------+  |
    |                                                       |
    +-------------------------------------------------------+
```

## Topics

### Initializers
- [init(instructions: Text?, links: [LinkItem], header: () -> Header)](./linkview/init%28instructions,links,header%29.md)
  Create an instance.
- [init(title: Text, detail: Text?, instructions: Text?, links: [LinkItem])](./linkview/init%28title,detail,instructions,links%29.md)
  Create an instance.
### Instance Properties
- [var body: some View](./linkview/body.md)
### Default Implementations
- [View Implementations](./linkview/view-implementations.md)
- [View Implementations](./linkview/view-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- SwiftUICore.View

## See Also

### Links
- [enum LinkItem](./linkitem.md)
  A link item tied to a button in the `LinkView`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview)*