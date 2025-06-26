# dragContainer(for:id:in:_:)

**Framework**: FamilyControls  
**Kind**: method

A container with draggable views. The drag payload is based on the current selection.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func dragContainer<ItemID, Item, Data>(for itemType: Item.Type = Item.self, id: @escaping (Item) -> ItemID, in namespace: Namespace.ID? = nil, _ payload: @escaping (ItemID) -> Data) -> some View where ItemID : Hashable, ItemID : Sendable, Item : Transferable, Item == Data.Element, Data : Collection
```

#### Return Value

A view that can be activated as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

Below is an example of a container view with three sections. Each section is draggable. Also, each section is selectable, and each view in a section is selectable as well. When a section drag starts, the app wants to use its custom logic to decide what the payload should be. If an unselected section is dragged, it should be the only one on the drag payload. If a selected section is dragged, the payload should contain other selected sections, and also the sections that have at least one fruit selected.

```swift
 var berries: [Fruit]
 var citruses: [Fruit]
 var tropical: [Fruit]

 @State var selectedSections: [UUID]
 @State var selectedFruits: [UUID]

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

 func sectionIDsToDrag(for draggedID: UUID) -> [UUID] {
     // an unselected section is dragged
     if !selectedSections.contains(draggedID) { return [draggedID] }

     // a selected section is dragged
     let payloadIDs = selectedSections + sectionIdentifiersOfSelectedFruits()
     return uniqueSections(from: payloadIDs)
 }

 func sections(identifiers: [UUID]) -> [FruitSection] { ... }
 func uniqueSections(from: [UUID]) -> [UUID] { ... }
 func sectionIdentifiersOfSelectedFruits() -> [UUID] { ... }

 struct Fruit {
     let id: UUID
 }

 struct FruitSection: Transferable {
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

- `itemType`: A type of the dragged item.
- `namespace`: An optional namespace that identifies the drag container.
- `id`: A closure that provides the item’s identifier.
- `payload`: A closure which is called when   a drag operation begins. As an argument, the closure receives the identifier   of the dragged view under the finger or cursor. Using   the passed identifier, put together the payload to drag,   and return from the closure.   Return an empty   to disable the drag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/dragcontainer(for:id:in:_:))*