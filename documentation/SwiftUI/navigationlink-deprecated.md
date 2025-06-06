# Deprecated symbols

**Framework**: SwiftUI

Review deprecated navigation link initializers.

#### Overview

For information about updating your use of navigation symbols, see [`Migrating to new navigation types`](migrating-to-new-navigation-types.md).

## Topics

### Creating links with view builders
- [init(_:isActive:destination:)](navigationlink/init(_:isactive:destination:).md)
  Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key.
- [init(isActive: Binding<Bool>, destination: () -> Destination, label: () -> Label)](navigationlink/init(isactive:destination:label:).md)
  Creates a navigation link that presents the destination view when active.
- [init(_:tag:selection:destination:)](navigationlink/init(_:tag:selection:destination:).md)
  Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string.
- [init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination, label: () -> Label)](navigationlink/init(tag:selection:destination:label:).md)
  Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value.
### Creating links for WatchKit
- [init(destinationName: String, isActive: Binding<Bool>, label: () -> Label)](navigationlink/init(destinationname:isactive:label:).md)
  Creates a navigation link that presents a view from a WatchKit storyboard when active.
- [init<V>(destinationName: String, tag: V, selection: Binding<V?>, label: () -> Label)](navigationlink/init(destinationname:tag:selection:label:).md)
  Creates a navigation link that presents a view from a WatchKit storyboard when a bound selection variable matches a value you provide.
- [init(destinationName: String, label: () -> Label)](navigationlink/init(destinationname:label:).md)
  Creates a navigation link that presents a view from a WatchKit storyboard.
### Creating links with view arguments
- [init(_:destination:isActive:)](navigationlink/init(_:destination:isactive:).md)
  Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key.
- [init(destination: Destination, isActive: Binding<Bool>, label: () -> Label)](navigationlink/init(destination:isactive:label:).md)
  Creates a navigation link that presents the destination view when active.
- [init(_:destination:tag:selection:)](navigationlink/init(_:destination:tag:selection:).md)
  Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string.
- [init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: () -> Label)](navigationlink/init(destination:tag:selection:label:).md)
  Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink-deprecated)*