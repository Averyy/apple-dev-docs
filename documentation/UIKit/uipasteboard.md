# UIPasteboard

**Framework**: UIKit  
**Kind**: class

An object that helps a user share data from one place to another within your app, and from your app to other apps.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class UIPasteboard
```

#### Overview

For sharing data with any other app, use the systemwide general pasteboard. For sharing data with another app from your team — that has the same team ID as the app to share from — configure an App Group. For more information about configuring an App Group, see [`Configuring app groups`](https://developer.apple.com/documentation/Xcode/configuring-app-groups).

In typical usage, an object in your app writes data to a pasteboard when the user requests a copy, cut, or duplicate operation on a selection in the user interface. Another object in the same or different app then reads that data from the pasteboard and presents it to the user at a new location. This usually happens when the user requests a paste operation.

> ❗ **Important**:  Starting in iOS 14, the system notifies the user when an app gets general pasteboard content that originates in a different app without . The system determines user intent based on user interactions, such as tapping a system-provided control or pressing Command-V. Use the properties and methods below to determine whether pasteboard items match various patterns, such as web search terms, URLs, or numbers, without notifying the user.

##### The General Pasteboard and Named Pasteboards

The system identifies the systemwide general pasteboard with the [`general`](uipasteboard/name-swift.struct/general.md) pasteboard name, and you can use it for any type of data. Obtain the general pasteboard from the [`general`](uipasteboard/general.md) shared system pasteboard object.

You can create named pasteboards with the class methods [`init(name:create:)`](uipasteboard/init(name:create:).md) and [`withUniqueName()`](uipasteboard/withuniquename().md) for sharing data within your app, and from your app to other apps that have the same Team ID.

##### Using Pasteboards

The [`UIPasteboard`](uipasteboard.md) class provides methods for reading and writing individual pasteboard items, as well as methods for reading and writing multiple pasteboard items at once. For more information, see [`Getting and setting pasteboard items`](uipasteboard#Getting-and-setting-pasteboard-items.md) in the topic groups below. The data to write to a pasteboard can be in one of the following forms:

- If the data is an object that conforms to [`NSItemProviderWriting`](https://developer.apple.com/documentation/Foundation/NSItemProviderWriting), use [`setItemProviders(_:localOnly:expirationDate:)`](uipasteboard/setitemproviders(_:localonly:expirationdate:).md) to write it to the pasteboard.
- If you can represent the data with a common object — such as [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate), [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), [`UIImage`](uiimage.md), or [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) — you can write it to the pasteboard as a value using a method such as [`setValue(_:forPasteboardType:)`](uipasteboard/setvalue(_:forpasteboardtype:).md).
- If the data is binary, use the [`setData(_:forPasteboardType:)`](uipasteboard/setdata(_:forpasteboardtype:).md) method to write it to the pasteboard.

The [`UIPasteboard`](uipasteboard.md) class provides convenience methods for writing and reading strings, images, URLs, and colors to and from single or multiple pasteboard items. See [`Getting and setting pasteboard items of standard data types`](uipasteboard#Getting-and-setting-pasteboard-items-of-standard-data-types.md) in the topic groups below.

> **Note**:  Before you attempt to read a particular data type from a pasteboard by using the methods in [`Getting and setting pasteboard items of standard data types`](uipasteboard#Getting-and-setting-pasteboard-items-of-standard-data-types.md) in the topic groups below, check for the presence of data of the type you want. Do this by using the type-checking methods.

[`UIPasteboard`](uipasteboard.md) provides properties for directly checking whether specific data types are present on a pasteboard, see [`Checking for data types on a pasteboard`](uipasteboard#Checking-for-data-types-on-a-pasteboard.md) in the topic groups below. Use these properties, rather than attempting to read pasteboard data, to avoid causing the system to needlessly attempt to fetch data before necessary, or when the data might not be present. For example, use the [`hasStrings`](uipasteboard/hasstrings.md) property to determine whether to present a string-data paste option in the user interface, using code like the following:

```objc
if UIPasteboard.general.hasStrings {
    // Enable string-related control...
}
```

Use the following properties to avoid user notifications and alerts when the system doesn’t establish user intent:

- [`numberOfItems`](uipasteboard/numberofitems.md)
- [`types`](uipasteboard/types.md), [`types(forItemSet:)`](uipasteboard/types(foritemset:).md)
- [`itemSet(withPasteboardTypes:)`](uipasteboard/itemset(withpasteboardtypes:).md)
- [`hasColors`](uipasteboard/hascolors.md), [`hasImages`](uipasteboard/hasimages.md), [`hasStrings`](uipasteboard/hasstrings.md), [`hasURLs`](uipasteboard/hasurls.md)
- [`canLoadObject(ofClass:)`](https://developer.apple.com/documentation/Foundation/NSItemProvider/canLoadObject(ofClass:)-3eig9), [`canLoadObject(ofClass:)`](https://developer.apple.com/documentation/Foundation/NSItemProvider/canLoadObject(ofClass:)-40grc)
- any of the pattern-detection methods in the [`Detecting patterns of content in pasteboard items`](uipasteboard#Detecting-patterns-of-content-in-pasteboard-items.md) group in the topic groups below

The system notifies the user when you access properties or call methods that pull data from the pasteboard if the system doesn’t determine that the user intends to access that data.

##### Pasteboard Items and Representation Types

When you write an object to a pasteboard, the pasteboard stores it as a . A pasteboard item consists of one or more key-value pairs in which the key identifies the representation type (sometimes called a ) of the value.

A uniform type identifier frequently functions as the key for a representation type. For example, you can use the [`UTTypeJPEG`](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTTypeJPEG) uniform type identifier (a constant for `public.jpeg`) as a representation type key for JPEG data.

For a discussion of uniform type identifiers, and a list of common ones, see [`Uniform Type Identifiers`](https://developer.apple.com/documentation/UniformTypeIdentifiers).

Your app can use any string to name a representation type; however, for app-specific data types, it’s best practice to use reverse-DNS notation to ensure the uniqueness of the type (for example, `com.myCompany.myApp.myType`).

You can provide flexibility for data sharing by providing multiple representation types for a pasteboard item during a copy or cut operation. Various contexts within your app or other apps can then make use of an appropriate representation type. For example, when a user copies an image, your app can write multiple representation types, such as in the PNG, JPEG, and GIF data formats, to a pasteboard. If the original image is in PNG format, but the receiving app can handle only GIF images, it can still use the pasteboard data.

For more about representation types, read the discussion for the [`types`](uipasteboard/types.md) instance method.

##### Sharing Pasteboards Between Devices

When a user signs into iCloud, the general pasteboard automatically transfers its contents to nearby devices that use the same iCloud account. You can control Handoff behavior when writing contents to the general pasteboard, and can set an expiration for items, using the [`setItemProviders(_:localOnly:expirationDate:)`](uipasteboard/setitemproviders(_:localonly:expirationdate:).md), [`setObjects(_:localOnly:expirationDate:)`](uipasteboard/setobjects(_:localonly:expirationdate:)-3h3iz.md), or [`setItems(_:options:)`](uipasteboard/setitems(_:options:).md) methods, as follows:

- To exclude a pasteboard from Handoff, specify [`false`](https://developer.apple.com/documentation/swift/false) for the `localOnly` parameter, or call the [`setItems(_:options:)`](uipasteboard/setitems(_:options:).md) method with the [`localOnly`](uipasteboard/optionskey/localonly.md) option.
- To indicate an expiration time and date for copied data, provide the `expirationDate` parameter, or call the [`setItems(_:options:)`](uipasteboard/setitems(_:options:).md) method with the [`expirationDate`](uipasteboard/optionskey/expirationdate.md) option. At the time and date that you set, the system removes the pasteboard items from the pasteboard.

##### Using Pasteboards with Other Objects

Although the [`UIPasteboard`](uipasteboard.md) class is central to copy, paste, and duplicate operations, you can employ protocols and instances of other UIKit classes in these operations as well, such as the following:

- [`UIEditMenuInteraction`](uieditmenuinteraction.md) — Displays a menu with edit actions, such as Copy, Cut, Paste, Select, and Select All, above or below the selection.
- [`UIActivityItemsConfigurationReading`](uiactivityitemsconfigurationreading.md) — Objects implement this protocol to indicate that they support copying and sharing data.
- [`UIPasteConfigurationSupporting`](uipasteconfigurationsupporting.md) — Objects implement this protocol to indicate whether they support pasting with a specific [`UIPasteConfiguration`](uipasteconfiguration.md).
- [`UIResponder`](uiresponder.md) — Responders implement [`canPerformAction(_:withSender:)`](uiresponder/canperformaction(_:withsender:).md) to enable or disable commands in the above-mentioned menu based on the current context.
- [`UIResponderStandardEditActions`](uiresponderstandardeditactions.md) — Responders implement methods that this informal protocol declares to handle the chosen menu commands (for example, `copy:` and `paste:`).

A typical app that implements copy, paste, and duplicate operations also manages and presents related selections in its user interface. In addition, your app needs to coordinate changes in pasteboard content with changes to its data model, as appropriate for your app.

## Topics

### Getting and removing pasteboards
- [class var general: UIPasteboard](uipasteboard/general.md)
  The systemwide general pasteboard, which you use for general copy-paste operations.
- [init?(name: UIPasteboard.Name, create: Bool)](uipasteboard/init(name:create:).md)
  Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.
- [class func withUniqueName() -> UIPasteboard](uipasteboard/withuniquename.md)
  Returns an app pasteboard that you identify by a unique system-generated name.
- [class func remove(withName: UIPasteboard.Name)](uipasteboard/remove(withname:).md)
  Invalidates the designated app pasteboard.
### Getting and setting pasteboard attributes
- [var name: UIPasteboard.Name](uipasteboard/name-swift.property.md)
  The name of the pasteboard.
- [var changeCount: Int](uipasteboard/changecount.md)
  The number of times the pasteboard’s contents change.
### Detecting patterns of content in pasteboard items
- [func detectPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: (Result<Set<PartialKeyPath<UIPasteboard.DetectedValues>>, any Error>) -> ())](uipasteboard/detectpatterns(for:completionhandler:)-23vwn.md)
  Requests that the data detection system identify the patterns that you specify for the pasteboard, and provide the patterns that it matches to your closure.
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<UIPasteboard.DetectedValues>>](uipasteboard/detectedpatterns(for:).md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard, and return the patterns that it matches.
- [func detectPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?, completionHandler: (Result<[Set<PartialKeyPath<UIPasteboard.DetectedValues>>], any Error>) -> ())](uipasteboard/detectpatterns(for:initemset:completionhandler:)-7ubl1.md)
  Requests that the data detection system identify the patterns that you specify for the pasteboard items, and provide the patterns that it matches to your closure.
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [Set<PartialKeyPath<UIPasteboard.DetectedValues>>]](uipasteboard/detectedpatterns(for:initemset:).md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard items, and return the patterns that it matches.
- [func detectValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: (Result<UIPasteboard.DetectedValues, any Error>) -> ())](uipasteboard/detectvalues(for:completionhandler:)-6adre.md)
  Requests that the data detection system identify the types of data that you specify for the pasteboard, and provide the values that it matches to your closure.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> UIPasteboard.DetectedValues](uipasteboard/detectedvalues(for:).md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard, and return the values that it matches.
- [func detectValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?, completionHandler: (Result<[UIPasteboard.DetectedValues], any Error>) -> ())](uipasteboard/detectvalues(for:initemset:completionhandler:)-pm9l.md)
  Requests that the data detection system identify the types of data that you specify for the pasteboard items, and provide the values that it matches to your closure.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [UIPasteboard.DetectedValues]](uipasteboard/detectedvalues(for:initemset:).md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard item, and return the values that it matches for each pasteboard.
- [UIPasteboard.DetectedValues](uipasteboard/detectedvalues.md)
  An object that contains common types of data that the data detection system matches for a pasteboard.
- [UIPasteboard.DetectionPattern](uipasteboard/detectionpattern.md)
  An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.
### Determining types of pasteboard items
- [var types: [String]](uipasteboard/types.md)
  The types of the first item on the pasteboard.
- [func types(forItemSet: IndexSet?) -> [[String]]?](uipasteboard/types(foritemset:).md)
  Returns an array of representation types for each specified pasteboard item.
- [func contains(pasteboardTypes: [String]) -> Bool](uipasteboard/contains(pasteboardtypes:).md)
  Returns whether the pasteboard holds data of the specified representation type.
- [func contains(pasteboardTypes: [String], inItemSet: IndexSet?) -> Bool](uipasteboard/contains(pasteboardtypes:initemset:).md)
  Returns whether the specified pasteboard items contain data of the given representation types.
- [func itemSet(withPasteboardTypes: [String]) -> IndexSet?](uipasteboard/itemset(withpasteboardtypes:).md)
  Returns an index set identifying pasteboard items having the specified representation types.
### Getting and setting pasteboard items
- [var numberOfItems: Int](uipasteboard/numberofitems.md)
  The number of items for the pasteboard.
- [var items: [[String : Any]]](uipasteboard/items.md)
  The pasteboard items on the pasteboard.
- [func addItems([[String : Any]])](uipasteboard/additems(_:).md)
  Appends pasteboard items to the current contents of the pasteboard.
- [func setItems([[String : Any]], options: [UIPasteboard.OptionsKey : Any])](uipasteboard/setitems(_:options:).md)
  Adds an array of items to a pasteboard, and sets privacy options for all the items on the pasteboard.
- [func data(forPasteboardType: String) -> Data?](uipasteboard/data(forpasteboardtype:).md)
  Returns the data on the pasteboard for the given representation type.
- [func data(forPasteboardType: String, inItemSet: IndexSet?) -> [Data]?](uipasteboard/data(forpasteboardtype:initemset:).md)
  Returns the data objects in the indicated pasteboard items that have the given representation type.
- [func setData(Data, forPasteboardType: String)](uipasteboard/setdata(_:forpasteboardtype:).md)
  Puts data on the pasteboard for the specified representation type.
- [func value(forPasteboardType: String) -> Any?](uipasteboard/value(forpasteboardtype:).md)
  Returns an object on the pasteboard for the given representation type.
- [func values(forPasteboardType: String, inItemSet: IndexSet?) -> [Any]?](uipasteboard/values(forpasteboardtype:initemset:).md)
  Returns the objects on the indicated pasteboard items that have the given representation type.
- [func setValue(Any, forPasteboardType: String)](uipasteboard/setvalue(_:forpasteboardtype:).md)
  Puts an object on the pasteboard for the specified representation type.
### Getting and setting pasteboard items of standard data types
- [var string: String?](uipasteboard/string.md)
  The string value of the first pasteboard item.
- [var strings: [String]?](uipasteboard/strings.md)
  An array of strings in all pasteboard items.
- [var image: UIImage?](uipasteboard/image.md)
  The image object of the first pasteboard item.
- [var images: [UIImage]?](uipasteboard/images.md)
  An array of image objects in all pasteboard items.
- [var url: URL?](uipasteboard/url.md)
  The URL object of the first pasteboard item.
- [var urls: [URL]?](uipasteboard/urls.md)
  An array of URL objects in all pasteboard items.
- [var color: UIColor?](uipasteboard/color.md)
  The color object of the first pasteboard item.
- [var colors: [UIColor]?](uipasteboard/colors.md)
  An array of color objects in all pasteboard items.
### Checking for data types on a pasteboard
- [var hasColors: Bool](uipasteboard/hascolors.md)
  A Boolean value that indicates whether the pasteboard contains contains a nonempty array of colors.
- [var hasImages: Bool](uipasteboard/hasimages.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of images.
- [var hasStrings: Bool](uipasteboard/hasstrings.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of strings.
- [var hasURLs: Bool](uipasteboard/hasurls.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of URLs.
### Getting and setting item providers
- [var itemProviders: [NSItemProvider]](uipasteboard/itemproviders.md)
  An array of item providers for the pasteboard.
- [func setItemProviders([NSItemProvider], localOnly: Bool, expirationDate: Date?)](uipasteboard/setitemproviders(_:localonly:expirationdate:).md)
  Sets and configures an explicit array of item providers for the pasteboard.
- [func setObjects([any NSItemProviderWriting])](uipasteboard/setobjects(_:)-lljo.md)
  Sets an array of item providers for the pasteboard, based on a specified array of objects.
- [func setObjects<T>([T])](uipasteboard/setobjects(_:)-fjg8.md)
  Sets an array of item providers for the pasteboard, based on a specified array of objects.
- [func setObjects([any NSItemProviderWriting], localOnly: Bool, expirationDate: Date?)](uipasteboard/setobjects(_:localonly:expirationdate:)-3h3iz.md)
  Sets and configures an array of item providers for the pasteboard, based on a specified array of objects.
- [func setObjects<T>([T], localOnly: Bool, expirationDate: Date?)](uipasteboard/setobjects(_:localonly:expirationdate:)-26u8o.md)
  Sets and configures an array of item providers for the pasteboard, based on a specified array of objects.
### Constants
- [UIPasteboard.Name](uipasteboard/name-swift.struct.md)
  Constants that identify the name of a pasteboard.
- [Pasteboard Names](pasteboard-names.md)
  Names identifying the system pasteboards.
- [UIPasteboard.OptionsKey](uipasteboard/optionskey.md)
  Options for describing pasteboard privacy.
- [Pasteboard Data Type Representations](pasteboard-data-type-representations.md)
  Pasteboard-item representation types, as for a given object value.
- [UserInfo Dictionary Keys](userinfo-dictionary-keys.md)
  Use these keys to access the representation types of pasteboard items that you add to, or remove from, a pasteboard.
### Notifications
- [class let changedNotification: NSNotification.Name](uipasteboard/changednotification.md)
  A notification that a pasteboard object posts when its contents change.
- [class let removedNotification: NSNotification.Name](uipasteboard/removednotification.md)
  A notification that a pasteboard object posts just before an app removes it.
### Deprecated
- [Deprecated symbols](uipasteboard-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Structures
- [UIPasteboard.ChangedMessage](uipasteboard/changedmessage.md)
- [UIPasteboard.RemovedMessage](uipasteboard/removedmessage.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIPasteControl](uipastecontrol.md)
  A button that a person taps to place pasteboard contents in your app.
- [UIPasteControl.Configuration](uipastecontrol/configuration-swift.class.md)
  An object that determines a paste button’s color, corner style, icon, and text.
- [UIPasteControl.DisplayMode](uipastecontrol/displaymode.md)
  Options that determine whether a paste button composes an icon, textual label, or both.
- [class UIPasteConfiguration](uipasteconfiguration.md)
  The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.
- [protocol UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
  The interface that determines whether a responder object supports paste configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard)*