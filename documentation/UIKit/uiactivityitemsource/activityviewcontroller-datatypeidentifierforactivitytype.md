# activityViewController(_:dataTypeIdentifierForActivityType:)

**Framework**: UIKit  
**Kind**: method

For items that are provided as data, returns the UTI for the item.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
optional func activityViewController(_ activityViewController: UIActivityViewController, dataTypeIdentifierForActivityType activityType: UIActivity.ActivityType?) -> String
```

#### Return Value

The UTI for the item.

#### Discussion

Providing the UTI allows services to handle specific data types in appropriate ways, such as an email service formatting an image to display in-line. If you provide items as [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) objects, implement this method to allow those services to better handle your data.

To ensure that Mail can handle an attachment that uses your exported UTI, include the [`UTExportedTypeDeclarations`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/UTExportedTypeDeclarations) key in your app’s `Info.plist` file, describing the UTI and providing the MIME type for it. The following example shows how `public.jpeg` might be defined as an exported type (only the required keys are shown):

```objc
<key>UTExportedTypeDeclarations</key>
        <array>
            <dict>
                <key>UTTypeIdentifier</key>
                <string>public.jpeg</string>
                <key>UTTypeConformsTo</key>
                <array>
                    <string>public.image</string>
                    <string>public.data</string>
                </array>
                <key>UTTypeTagSpecification</key>
                <dict>
                    <key>com.apple.ostype</key>
                    <string>JPEG</string>
                    <key>public.filename-extension</key>
                    <array>
                        <string>jpeg</string>
                        <string>jpg</string>
                    </array>
                    <key>public.mime-type</key>
                    <string>image/jpeg</string>
                </dict>
            </dict>
        </array>
```

## Parameters

- `activityViewController`: The activity view controller object requesting information about the data item.
- `activityType`: The selected activity type; may be  .

## See Also

- [func activityViewController(UIActivityViewController, subjectForActivityType: UIActivity.ActivityType?) -> String](uiactivityitemsource/activityviewcontroller(_:subjectforactivitytype:).md)
  For activities that support a subject field, returns the subject for the item.
- [func activityViewController(UIActivityViewController, thumbnailImageForActivityType: UIActivity.ActivityType?, suggestedSize: CGSize) -> UIImage?](uiactivityitemsource/activityviewcontroller(_:thumbnailimageforactivitytype:suggestedsize:).md)
  For activities that support a preview image, returns a thumbnail preview image for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontroller(_:datatypeidentifierforactivitytype:))*