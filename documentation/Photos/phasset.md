# PHAsset

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A representation of an image, video, or Live Photo in the Photos library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHAsset
```

```objc
@interface PHAsset : PHObject
```

## Mentions

- [Fetching Objects and Requesting Changes](../PhotoKit/fetching-objects-and-requesting-changes.md)
- [Requesting Changes to the Photo Library](../PhotoKit/requesting-changes-to-the-photo-library.md)
- [Displaying Live Photos](../PhotoKit/displaying-live-photos.md)
- [Fetching Assets](../PhotoKit/fetching-assets.md)

#### Overview

You fetch assets to begin working with them. Use the class methods listed in Fetching Assets to retrieve one or more [`PHAsset`](./phasset.md) instances representing the assets you want to display or edit.

Assets contain only metadata. The underlying image or video data for any given asset might not be stored on the local device. However, depending on how you plan to use this data, you may not need to download all of it. If you need to populate a collection view with thumbnail images, the Photos framework can manage downloading, generating, and caching thumbnails for each asset. For details, see [`PHImageManager`](./phimagemanager.md).

Asset objects are immutable. To edit an asset’s metadata (such as marking it as a favorite photo), create a [`PHAssetChangeRequest`](./phassetchangerequest.md) object within a photo library change block. For more details on using change requests and change blocks to update the photo library, see [`PHPhotoLibrary`](./phphotolibrary.md).

## Topics

### Fetching Assets
- [Fetching Assets](../PhotoKit/fetching-assets.md)
  Retrieve asset metadata or request full asset content.
- [class func fetchAssets(in: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./phasset/fetchassets%28in,options%29.md)
  Retrieves assets from the specified asset collection.
- [class func fetchAssets(with: PHAssetMediaType, options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./phasset/fetchassets%28with,options%29.md)
  Retrieves assets with the specified media type.
- [class func fetchAssets(withLocalIdentifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./phasset/fetchassets%28withlocalidentifiers,options%29.md)
  Retrieves assets with the specified local-device-specific unique identifiers.
- [class func fetchKeyAssets(in: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHAsset>?](./phasset/fetchkeyassets%28in,options%29.md)
  Retrieves assets marked as key assets in the specified asset collection.
- [class func fetchAssets(with: PHFetchOptions?) -> PHFetchResult<PHAsset>](./phasset/fetchassets%28with%29.md)
  Retrieves all assets matching the specified options.
- [class func fetchAssets(withBurstIdentifier: String, options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./phasset/fetchassets%28withburstidentifier,options%29.md)
  Retrieves assets with the specified burst photo sequence identifier.
- [class func fetchAssets(withALAssetURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./phasset/fetchassets%28withalasseturls,options%29.md)
  Retrieves assets using URLs provided by the Assets Library framework.
### Reading Asset Metadata
- [var contentType: UTType](./phasset/contenttype.md)
  The type of image or video data that is presented for the asset
- [var mediaType: PHAssetMediaType](./phasset/mediatype.md)
  The type of the asset, such as video or audio.
- [enum PHAssetMediaType](./phassetmediatype.md)
  Identifies the general type of an asset, such as image or video.
- [var mediaSubtypes: PHAssetMediaSubtype](./phasset/mediasubtypes.md)
  The subtypes of the asset, identifying special kinds of assets, such as panoramic photo or high-frame-rate video.
- [struct PHAssetMediaSubtype](./phassetmediasubtype.md)
  Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.
- [var sourceType: PHAssetSourceType](./phasset/sourcetype.md)
  The means by which the asset enters the user’s Photos library.
- [struct PHAssetSourceType](./phassetsourcetype.md)
  The means by which an asset enters the Photos library.
- [var pixelWidth: Int](./phasset/pixelwidth.md)
  The width, in pixels, of the asset’s image or video data.
- [var pixelHeight: Int](./phasset/pixelheight.md)
  The height, in pixels, of the asset’s image or video data.
- [var addedDate: Date?](./phasset/addeddate.md)
  The date and time this asset was added to the photo library (from the device that was used to add this asset)
- [var creationDate: Date?](./phasset/creationdate.md)
  The date and time of the asset’s creation.
- [var modificationDate: Date?](./phasset/modificationdate.md)
  The date and time of the asset’s last modification.
- [var location: CLLocation?](./phasset/location.md)
  The location information for the asset.
- [var duration: TimeInterval](./phasset/duration.md)
  The duration, in seconds, of the video asset.
- [var isFavorite: Bool](./phasset/isfavorite.md)
  A Boolean value that indicates whether the user marks the asset as a favorite.
- [var isHidden: Bool](./phasset/ishidden.md)
  A Boolean value that indicates whether the user hides the asset.
- [var hasAdjustments: Bool](./phasset/hasadjustments.md)
  A Boolean value that indicates whether the asset contains adjustment data.
- [var adjustmentFormatIdentifier: String?](./phasset/adjustmentformatidentifier.md)
  The identifier that describes the adjustment format.
- [var isSyncFailureHidden: Bool](./phasset/issyncfailurehidden.md)
  A Boolean value that indicates whether the user hides the sync failure message.
- [var extendedMetadata: PHAssetExtendedMetadata](./phasset/extendedmetadata.md)
  An accessor to other asset properties.
- [class PHAssetExtendedMetadata](./phassetextendedmetadata.md)
  Represents other asset attributes that are not included when fetching `PHAsset` directly.
- [var rating: PHAsset.Rating](./phasset/rating-swift.property.md)
  The rating of this PHAsset.
- [PHAsset.Rating](./phasset/rating-swift.enum.md)
  A rating for an asset, from unset (no rating chosen) up to five stars.
### Displaying an Asset
- [var playbackStyle: PHAsset.PlaybackStyle](./phasset/playbackstyle-swift.property.md)
  An enumerated value that describes how to present an asset to the user.
- [PHAsset.PlaybackStyle](./phasset/playbackstyle-swift.enum.md)
  An enumeration of asset playback styles that dictate how to present an asset to the user.
### Editing an Asset
- [Editing Asset Content](../PhotoKit/editing-asset-content.md)
  Make a request to modify and save a photo or video asset.
- [class PHContentEditingInput](./phcontenteditinginput.md)
  A container that provides information about and access to the image, video, or Live Photo content of an asset to be edited.
- [class PHContentEditingOutput](./phcontenteditingoutput.md)
  A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.
- [class PHAdjustmentData](./phadjustmentdata.md)
  A description of the edits made to an asset’s photo, video, or Live Photo content, which allows your app to reconstruct or revert the effects of prior editing sessions.
- [class PHContentEditingInputRequestOptions](./phcontenteditinginputrequestoptions.md)
  A set of options affecting the delivery of image or video data when you request to edit the content of a Photos asset.
- [class PHLivePhotoEditingContext](./phlivephotoeditingcontext.md)
  An editing session for modifying the photo, video, and audio content of a Live Photo.
- [protocol PHLivePhotoFrame](./phlivephotoframe.md)
  A container that provides image content for a single frame of a Live Photo in an editing context.
- [func canPerform(PHAssetEditOperation) -> Bool](./phasset/canperform%28_%29.md)
  Returns whether the asset supports the specified editing operation.
- [enum PHAssetEditOperation](./phasseteditoperation.md)
  Values identifying possible actions an asset can support, used by the [`canPerform(_:)`](./phasset/canperform%28_%29.md) method.
- [func requestContentEditingInput(with: PHContentEditingInputRequestOptions?, completionHandler: (PHContentEditingInput?, [AnyHashable : Any]) -> Void) -> PHContentEditingInputRequestID](./phasset/requestcontenteditinginput%28with,completionhandler%29.md)
  Requests asset information for beginning a content editing session.
- [func cancelContentEditingInputRequest(PHContentEditingInputRequestID)](./phasset/cancelcontenteditinginputrequest%28_%29.md)
  Cancels a request for editing the asset’s content.
- [typealias PHContentEditingInputRequestID](./phcontenteditinginputrequestid.md)
  An identifier for an asset content editing session.
- [PHAsset.OriginalResourceChoice](./phasset/originalresourcechoice-swift.enum.md)
  A choice of which original resource to use as the unadjusted base when reverting an asset’s content.
- [Editing Request Info Keys](../PhotoKit/editing-request-info-keys.md)
  Keys indicating the status of an asset content editing request, used in the completion handler of the [`requestContentEditingInput(with:completionHandler:)`](./phasset/requestcontenteditinginput%28with,completionhandler%29.md) method.
### Working with Burst Photo Assets
- [var burstIdentifier: String?](./phasset/burstidentifier.md)
  The unique identifier shared by photo assets from the same burst sequence.
- [var burstSelectionTypes: PHAssetBurstSelectionType](./phasset/burstselectiontypes.md)
  The selection type of the asset in a burst photo sequence.
- [struct PHAssetBurstSelectionType](./phassetburstselectiontype.md)
  Bit mask values indicating whether and how an asset is marked as a favorite member of a burst photo sequence. Used by the [`burstSelectionTypes`](./phasset/burstselectiontypes.md) property.
- [var representsBurst: Bool](./phasset/representsburst.md)
  A Boolean value that indicates whether the asset is the representative photo from a burst photo sequence.
### Instance Properties
- [var adjustmentTimestamp: Date?](./phasset/adjustmenttimestamp.md)
  The date when the asset was last edited.
- [var adjustmentsState: PHAsset.AdjustmentsState](./phasset/adjustmentsstate-swift.property.md)
- [var originalResourceChoice: PHAsset.OriginalResourceChoice](./phasset/originalresourcechoice-swift.property.md)
  The original resource used as the basis for rendering this asset’s derivatives.
- [var playbackVariation: PHAsset.PlaybackVariation](./phasset/playbackvariation-swift.property.md)
  The Live Photo playback variation for the asset.
### Type Aliases
- [typealias Specification](./phasset/specification.md)
- [typealias UnwrappedType](./phasset/unwrappedtype.md)
- [typealias ValueType](./phasset/valuetype.md)
### Type Properties
- [static let defaultResolverSpecification: EmptyResolverSpecification<PHAsset>](./phasset/defaultresolverspecification.md)
### Enumerations
- [PHAsset.AdjustmentsState](./phasset/adjustmentsstate-swift.enum.md)
- [PHAsset.PlaybackVariation](./phasset/playbackvariation-swift.enum.md)
### Default Implementations
- [PersistentlyIdentifiable Implementations](./phasset/persistentlyidentifiable-implementations.md)

## Relationships

### Inherits From
- [PHObject](./phobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/customlocalizedstringresourceconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [DisplayRepresentable](../AppIntents/displayrepresentable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [InstanceDisplayRepresentable](../AppIntents/instancedisplayrepresentable.md)
- [IntentValueConvertible](../AppIntents/intentvalueconvertible.md)
- [IntentValueExpressing](../AppIntents/intentvalueexpressing.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [PersistentlyIdentifiable](../AppIntents/persistentlyidentifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TypeDisplayRepresentable](../AppIntents/typedisplayrepresentable.md)

## See Also

### Asset retrieval
- [Fetching Objects and Requesting Changes](../PhotoKit/fetching-objects-and-requesting-changes.md)
  Get assets, asset collections, and collection lists matching a specified query.
- [class PHAssetCollection](./phassetcollection.md)
  A representation of a Photos asset grouping, such as Moments, a user-created album, or a Smart Album.
- [class PHCollection](./phcollection.md)
  The abstract superclass for Photos asset collections and collection lists.
- [class PHCollectionList](./phcollectionlist.md)
  A group containing Photos asset collections, such as Moments, Years, or folders of user-created albums.
- [class PHObject](./phobject.md)
  The abstract superclass for Photos model objects, including assets and collections.
- [class PHFetchResult](./phfetchresult.md)
  An ordered list of assets or collections returned from a Photos fetch method.
- [class PHFetchOptions](./phfetchoptions.md)
  A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset)*