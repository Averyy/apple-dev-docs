# Deprecated modifiers

**Framework**: SwiftUI  
**Role**: API Collection

Review unsupported modifiers and their replacements.

#### Overview

Avoid using deprecated modifiers in your app. Select a modifier to see the replacement that you should use instead.

## Topics

### Accessibility modifiers
- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibility%28label%29.md)
  Adds a label to the view that describes its contents.
- [func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibility%28value%29.md)
  Adds a textual description of the value that the view contains.
- [func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibility%28hidden%29.md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibility%28identifier%29.md)
  Uses the specified string to identify the view.
- [func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibility%28selectionidentifier%29.md)
  Sets a selection identifier for this view’s accessibility element.
- [func accessibility(hint: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibility%28hint%29.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibility(activationPoint:)](./view/accessibility%28activationpoint%29.md)
  Specifies the point where activations occur in the view.
- [func accessibility(inputLabels: [Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibility%28inputlabels%29.md)
  Sets alternate input labels with which users identify a view.
- [func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibility%28addtraits%29.md)
  Adds the given traits to the view.
- [func accessibility(removeTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibility%28removetraits%29.md)
  Removes the given traits from this view.
- [func accessibility(sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibility%28sortpriority%29.md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
### Appearance modifiers
- [func colorScheme(ColorScheme) -> some View](./view/colorscheme%28_%29.md)
  Sets this view’s color scheme.
- [func listRowPlatterColor(Color?) -> some View](./view/listrowplattercolor%28_%29.md)
  Sets the color that the system applies to the row background when this view is placed in a list.
- [func background<Background>(Background, alignment: Alignment) -> some View](./view/background%28_,alignment%29.md)
  Layers the given view behind this view.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](./view/overlay%28_,alignment%29.md)
  Layers a secondary view in front of this view.
- [func foregroundColor(Color?) -> some View](./view/foregroundcolor%28_%29.md)
  Sets the color of the foreground elements displayed by this view.
- [func complicationForeground() -> some View](./view/complicationforeground%28%29.md)
  Promotes this view to the foreground in a complication.
### Text modifiers
- [func autocapitalization(UITextAutocapitalizationType) -> some View](./view/autocapitalization%28_%29.md)
  Sets whether to apply auto-capitalization to this view.
- [func disableAutocorrection(Bool?) -> some View](./view/disableautocorrection%28_%29.md)
  Sets whether to disable autocorrection for this view.
### Auxiliary view modifiers
- [func navigationBarTitle(_:)](./view/navigationbartitle%28_%29.md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle(_:displayMode:)](./view/navigationbartitle%28_,displaymode%29.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](./view/navigationbaritems%28leading%29.md)
  Sets the navigation bar items for this view.
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](./view/navigationbaritems%28leading,trailing%29.md)
  Sets the navigation bar items for this view.
- [func navigationBarItems<T>(trailing: T) -> some View](./view/navigationbaritems%28trailing%29.md)
  Configures the navigation bar items for this view.
- [func navigationBarHidden(Bool) -> some View](./view/navigationbarhidden%28_%29.md)
  Hides the navigation bar for this view.
- [func statusBar(hidden: Bool) -> some View](./view/statusbar%28hidden%29.md)
  Sets the visibility of the status bar.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](./view/contextmenu%28_%29.md)
  Adds a context menu to the view.
### Style modifiers
- [func menuButtonStyle<S>(S) -> some View](./view/menubuttonstyle%28_%29.md)
  Sets the style for menu buttons within this view.
- [func navigationViewStyle<S>(S) -> some View](./view/navigationviewstyle%28_%29.md)
  Sets the style for navigation views within this view.
### Layout modifiers
- [func frame() -> some View](./view/frame%28%29.md)
  Positions this view within an invisible frame.
- [func edgesIgnoringSafeArea(Edge.Set) -> some View](./view/edgesignoringsafearea%28_%29.md)
  Changes the view’s proposed area to extend outside the screen’s safe areas.
- [func coordinateSpace<T>(name: T) -> some View](./view/coordinatespace%28name%29.md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
### Graphics and rendering modifiers
- [func accentColor(Color?) -> some View](./view/accentcolor%28_%29.md)
  Sets the accent color for this view and the views it contains.
- [func mask<Mask>(Mask) -> some View](./view/mask%28_%29.md)
  Masks this view using the alpha channel of the given view.
- [func animation(Animation?) -> some View](./view/animation%28_%29-1hc0p.md)
  Applies the given animation to all animatable values within this view.
- [func cornerRadius(CGFloat, antialiased: Bool) -> some View](./view/cornerradius%28_,antialiased%29.md)
  Clips this view to its bounding frame, with the specified corner radius.
### Input and events modifiers
- [func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool, isTargeted: (Bool) -> Void) -> some View](./view/dropdestination%28for,action,istargeted%29.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func onChange<V>(of: V, perform: (V) -> Void) -> some View](./view/onchange%28of,perform%29.md)
  Adds an action to perform when the given value changes.
- [func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform: (CGPoint) -> Void) -> some View](./view/ontapgesture%28count,coordinatespace,perform%29-36x9h.md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](./view/onlongpressgesture%28minimumduration,maximumdistance,pressing,perform%29.md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](./view/onlongpressgesture%28minimumduration,pressing,perform%29.md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) -> some View](./view/onpastecommand%28of,perform%29-4f78f.md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) -> Payload?, perform: (Payload) -> Void) -> some View](./view/onpastecommand%28of,validator,perform%29-964k1.md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.
- [func onDrop(of: [String], delegate: any DropDelegate) -> some View](./view/ondrop%28of,delegate%29-2vr9o.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate.
- [func onDrop(of:isTargeted:perform:)](./view/ondrop%28of,istargeted,perform%29.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View](./view/focusable%28_,onfocuschange%29.md)
  Specifies if the view is focusable and, if so, adds an action to perform when the view comes into focus.
- [func onContinuousHover(coordinateSpace: CoordinateSpace, perform: (HoverPhase) -> Void) -> some View](./view/oncontinuoushover%28coordinatespace,perform%29-8gyrl.md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
### View presentation modifiers
- [func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) -> some View](./view/actionsheet%28ispresented,content%29.md)
  Presents an action sheet when a given condition is true.
- [func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some View](./view/actionsheet%28item,content%29.md)
  Presents an action sheet using the given item as a data source for the sheet’s content.
- [func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View](./view/alert%28ispresented,content%29.md)
  Presents an alert to the user.
- [func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some View](./view/alert%28item,content%29.md)
  Presents an alert to the user.
### Search modifiers
- [func searchable(text:placement:prompt:suggestions:)](./view/searchable%28text,placement,prompt,suggestions%29.md)
  Marks this view as searchable, which configures the display of a search field.
### Tab modifiers
- [func tabItem<V>(() -> V) -> some View](./view/tabitem%28_%29.md)
  Sets the tab bar item associated with this view.
### Generating image modifiers
- [func imagePlaygroundPersonalizationPolicy(ImagePlaygroundPersonalizationPolicy) -> some View](./view/imageplaygroundpersonalizationpolicy%28_%29.md)
  Policy determining whether to support the usage of people in the playground or not.
### Technology-specific modifiers
- [func postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)](./view/posttophotossharedalbumsheet%28ispresented,items,photolibrary,defaultalbumidentifier,completion%29.md)
  Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View](./view/offercoderedemption%28ispresented,oncompletion%29.md)
- [func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> Product.SubscriptionOffer.Signature) -> some View](./view/subscriptionpromotionaloffer%28offer,signature%29.md)
  Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-deprecated)*