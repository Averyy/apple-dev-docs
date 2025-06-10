# dragContainer(for:in:_:)

**Framework**: Journaling Suggestions  
**Kind**: method

A container with draggable views. The drag payload is identifiable. To form the payload, use the identifier of the dragged view inside the container.

**Availability**:
- iOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func dragContainer<Item, Data>(for itemType: Item.Type = Item.self, in namespace: Namespace.ID? = nil, _ payload: @escaping (Item.ID) -> Data) -> some View where Item : Transferable, Item : Identifiable, Item == Data.Element, Data : Collection, Item.ID : Sendable
```

#### Return Value

A view that can be activated as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

Below is an example of a container view with three sections. Each section is draggable. Also, each section is selectable, and each view in a section is selectable as well. When a section drag starts, the app wants to use its custom logic to decide what the payload should be.

If an unselected section is dragged, it should be the only one on the drag payload. If a selected section is dragged, the payload should contain other selected sections, and also the sections that have at least one fruit selected.

```None
 var berries: [Fruit]
 var citruses: [Fruit]
 var tropical: [Fruit]

 @State var selectedSections: [FruitSection.ID]
 @State var selectedFruits: [Fruit.ID]

 var body: some View {
     ScrollView {
         VStack {
             BerriesSectionView(FruitSection(berries))
                 .draggable(containerItemID: FruitSection.berries)
             CitrusSectionView(FruitSection(citruses))
               .draggable(containerItemID: FruitSection.citruses)
             TropicalSectionView(FruitSection(tropical))
                 .draggable(containerItemID: FruitSection.tropical)
         }
     }
     .dragContainer { draggedSectionID in
         let identifiers = sectionIDsToDrag(for: draggedSectionID)
         return sections(identifiers: identifiers)
     }
 }

 func sectionIDsToDrag(for draggedID: FruitSection.ID) -> [FruitSection.ID] {
     // an unselected section is dragged
     if !selectedSections.contains(draggedID) { return [draggedID] }

     // a selected section is dragged
     let payloadIDs = selectedSections + sectionIdentifiersOfSelectedFruits()
     return uniqueSections(from: payloadIDs)
 }

 func sections(identifiers: [FruitSection.ID]) -> [FruitSection] { ... }
 func sectionIdentifiersOfSelectedFruits() -> [FruitSection.ID] { ... }
 func uniqueSections(from: [FruitSection.ID]) -> [FruitSection.ID] { ... }

 struct Fruit: Identifiable { ... }

 struct FruitSection: Transferable, Identifiable {
     static let berries: UUID
     static let citruses: UUID
     static let tropical: UUID

     let id: UUID
     var fruits: [Fruit]
 }

 struct BerriesSectionView: View {
     var section: FruitSection
     var body: some View {
         HStack {
             ForEach(section.fruit) { berry in
                 BerryView(berry)
             }
         }
     }
 }
```

## Parameters

- `itemType`: A type of the dragged items.
- `namespace`: A namespace that identifies the drag container.
- `payload`: A closure which is called when   a drag operation begins. As an argument, the closure receives the identifier   of the dragged view under the finger or cursor. Using   the passed identifier, put together the payload to drag,   and return from the closure.   Return an empty   to disable the drag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/dragcontainer(for:in:_:))*