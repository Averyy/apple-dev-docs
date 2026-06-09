# hidden(_:)

**Framework**: SwiftUI  
**Kind**: method

Hides the tab from the user.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func hidden(_ hidden: Bool = true) -> some TabContent<Self.TabValue>
```

#### Discussion

Unlike removing or adding tabs with `if` statements, this modifier preserves the associated state of the tab’s content view when the tab is hidden.

When you hide a tab using this modifier, make sure to update the TabView’s selection appropriately, since that tab could be selected.

The following example shows a `TabView` with 4 tabs in compact and 5 tabs in regular. In compact, one of the tabs is a ‘Browse’ tab that displays a custom list view. This list view allows navigating to the destinations that are contained within the ‘Library’ and ‘Playlists’ sections in regular. The navigation path and the selection state are updated when the number of tabs changes.

```swift
struct BrowseTabExample: View {
    @Environment(\.horizontalSizeClass) var sizeClass

    @State var selection: MusicTab = .listenNow
    @State var browseTabPath: [MusicTab] = []
    @State var playlists = [Playlist("All Playlists"), Playlist("Running")]

    var body: some View {
            TabView(selection: $selection) {
                Tab("Listen Now", systemImage: "play.circle", value: .listenNow) {
                    ListenNowView()
                }

                Tab("Radio", systemImage: "dot.radiowaves.left.and.right", value: .radio) {
                    RadioView()
                }

                Tab("Search", systemImage: "magnifyingglass", value: .search) {
                    SearchDetailView()
                }

                Tab("Browse", systemImage: "list.bullet", value: .browse) {
                    LibraryView(path: $browseTabPath)
                }
                .hidden(sizeClass != .compact)

                TabSection("Library") {
                    Tab("Recently Added", systemImage: "clock", value: MusicTab.library(.recentlyAdded)) {
                        RecentlyAddedView()
                    }

                    Tab("Artists", systemImage: "music.mic", value: MusicTab.library(.artists)) {
                        ArtistsView()
                    }
                }
                .hidden(sizeClass == .compact)

                TabSection("Playlists") {
                    ForEach(playlists) { playlist in
                        Tab(playlist.name, image: playlist.image, value: MusicTab.playlists(playlist)) {
                            playlist.detailView()
                        }
                    }
                }
                .hidden(sizeClass == .compact)
            }
            .tabViewStyle(.sidebarAdaptable)
            .onChange(of: sizeClass, initial: true) { _, sizeClass in
                if sizeClass == .compact && selection.showInBrowseTab {
                    browseTabPath = [selection]
                    selection = .browse
                } else if sizeClass == .regular && selection == .browse {
                    selection = browseTabPath.last ?? .library(.recentlyAdded)
                }
            }
        }
    }
}

struct LibraryView: View {
    @Binding var path: [MusicTab]

    var body: some View {
        NavigationStack(path: $path) {
            List {
                ForEach(MusicLibraryTab.allCases, id: \.self) { tab in
                    NavigationLink(tab.rawValue, value: MusicTab.library(tab))
                }
                // Code to add playlists here
            }
            .navigationDestination(for: MusicTab.self) { tab in
                tab.detail()
            }
        }
    }
}
```

## Parameters

- `hidden`: Whether the tab is hidden.

## See Also

- [func badge(_:)](tabcontent/badge(_:).md)
  Generates a badge for a tab from an integer value.
- [func contextMenu<M>(menuItems: () -> M) -> some TabContent<Self.TabValue>
](tabcontent/contextmenu(menuitems:).md)
  Adds a context menu to a tab.
- [func customizationBehavior(TabCustomizationBehavior, for: AdaptableTabBarPlacement...) -> some TabContent<Self.TabValue>
](tabcontent/customizationbehavior(_:for:).md)
  Configures the customization behavior of customizable tab view content.
- [func customizationID(String) -> some TabContent<Self.TabValue>
](tabcontent/customizationid(_:).md)
  Sets the identifier for a tab to persist its state.
- [func defaultSectionExpansion(TabSectionExpansion) -> some TabContent<Self.TabValue>
](tabcontent/defaultsectionexpansion(_:).md)
  Sets the default expansion state for the section containing this tab when displayed in the sidebar.
- [struct TabSectionExpansion](tabsectionexpansion.md)
  The default expansion state for a tab section in the sidebar.
- [func defaultVisibility(Visibility, for: AdaptableTabBarPlacement...) -> some TabContent<Self.TabValue>
](tabcontent/defaultvisibility(_:for:).md)
  Configures the default visibility of a tab in customizable contexts.
- [func disabled(Bool) -> some TabContent<Self.TabValue>
](tabcontent/disabled(_:).md)
  Controls whether users can interact with this tab.
- [func draggable<T>(@autoclosure () -> T) -> some TabContent<Self.TabValue>
](tabcontent/draggable(_:).md)
  Activates this tab as the source of a drag and drop operation. This tab can only be dragged when in the sidebar.
- [func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some TabContent<Self.TabValue>
](tabcontent/dropdestination(for:action:).md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func help(_:)](tabcontent/help(_:).md)
  Adds help text to a tab using a text view that you provide.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some TabContent<Self.TabValue>
](tabcontent/popover(ispresented:attachmentanchor:arrowedge:content:).md)
  Presents a popover when a given condition is true.
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some TabContent<Self.TabValue>
](tabcontent/popover(item:attachmentanchor:arrowedge:content:).md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func sectionActions<Content>(content: () -> Content) -> some TabContent<Self.TabValue>
](tabcontent/sectionactions(content:).md)
  Adds custom actions to a tab section.
- [func springLoadingBehavior(SpringLoadingBehavior) -> some TabContent<Self.TabValue>
](tabcontent/springloadingbehavior(_:).md)
  Sets the spring loading behavior for the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/hidden(_:))*