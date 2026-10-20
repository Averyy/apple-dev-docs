# buildBlock(_:_:_:_:_:_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(_ c0: C0, _ c1: C1, _ c2: C2, _ c3: C3, _ c4: C4, _ c5: C5, _ c6: C6) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands, C4 : Commands, C5 : Commands, C6 : Commands
```

## See Also

### Building content
- [static func buildBlock() -> EmptyCommands](./buildblock%28%29.md)
  Builds an empty command set from a block containing no statements.
- [static func buildBlock<C>(C) -> C](./buildblock%28_%29.md)
  Passes a single command group written as a child group through modified.
- [static func buildBlock<C0, C1>(C0, C1) -> some Commands](./buildblock%28_,_%29.md)
- [static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands](./buildblock%28_,_,_%29.md)
- [static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands](./buildblock%28_,_,_,_%29.md)
- [static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some Commands](./buildblock%28_,_,_,_,_%29.md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) -> some Commands](./buildblock%28_,_,_,_,_,_%29.md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4, C5, C6, C7) -> some Commands](./buildblock%28_,_,_,_,_,_,_,_%29.md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3, C4, C5, C6, C7, C8) -> some Commands](./buildblock%28_,_,_,_,_,_,_,_,_%29.md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9) -> some Commands](./buildblock%28_,_,_,_,_,_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandsbuilder/buildblock(_:_:_:_:_:_:_:))*