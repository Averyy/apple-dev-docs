# Photos

**Framework**: Photos  
**Kind**: module  
**Role**: Framework

Work with image and video assets that the Photos app manages, including those from iCloud Photos and Live Photos.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

#### Overview

Use PhotoKit to access image and video assets that the Photos app manages in iOS, macOS, tvOS, and visionOS. You might use this framework to edit or display a person’s photos, or to manage collections of assets such as albums, Moments, and Shared Albums. The framework provides access to photos on the person’s device and in iCloud.

> **Note**: Photos is a [PhotoKit](../PhotoKit/PhotoKit.md) framework.

## Topics

### Shared photo library
- [class PHPhotoLibrary](./phphotolibrary.md)
  An object that manages access and changes to a person’s photo library.
### Asset retrieval
- [Fetching Objects and Requesting Changes](../PhotoKit/fetching-objects-and-requesting-changes.md)
  Get assets, asset collections, and collection lists matching a specified query.
- [class PHAsset](./phasset.md)
  A representation of an image, video, or Live Photo in the Photos library.
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
### Asset loading
- [Loading and Caching Assets and Thumbnails](../PhotoKit/loading-and-caching-assets-and-thumbnails.md)
  Request image, video, or Live Photos content, and cache for quick reuse.
- [class PHImageManager](./phimagemanager.md)
  An object that facilitates retrieving or generating preview thumbnails and asset data.
- [class PHCachingImageManager](./phcachingimagemanager.md)
  An object that facilitates retrieving or generating preview thumbnails, optimized for batch preloading large numbers of assets.
- [class PHImageRequestOptions](./phimagerequestoptions.md)
  A set of options affecting the delivery of still image representations of Photos assets you request from an image manager.
- [class PHVideoRequestOptions](./phvideorequestoptions.md)
  A set of options affecting the delivery of video asset data that you request from an image manager.
- [class PHLivePhotoRequestOptions](./phlivephotorequestoptions.md)
  A set of options affecting the delivery of Live Photo assets you request from an image manager.
### Asset metadata
- [class PHAssetExtendedMetadata](./phassetextendedmetadata.md)
  Represents other asset attributes that are not included when fetching `PHAsset` directly.
### Asset resource management
- [class PHAssetResource](./phassetresource.md)
  An underlying data resource associated with a photo, video, or Live Photo asset in the Photos library.
- [class PHAssetCreationRequest](./phassetcreationrequest.md)
  A request to create a new Photos asset from underlying data resources, for use in a photo library change block.
- [class PHAssetResourceCreationOptions](./phassetresourcecreationoptions.md)
  A set of options affecting the creation of a new Photos asset from underlying resources.
- [class PHAssetResourceManager](./phassetresourcemanager.md)
  A resource manager for the data storage underlying a Photos asset.
- [class PHAssetResourceRequestOptions](./phassetresourcerequestoptions.md)
  A set of options affecting the delivery of underlying asset data that you request from the asset-resource manager.
### Background resource upload extensions
- [Uploading asset resources in the background](../PhotoKit/uploading-asset-resources-in-the-background.md)
  Enable reliable cloud backup for photo library assets with background processing.
- [protocol PHBackgroundResourceUploadExtension](./phbackgroundresourceuploadextension.md)
  A protocol to interact with asset resource upload jobs during background processing.
- [class PHAssetResourceUploadJob](./phassetresourceuploadjob.md)
  An object that represents a request to upload an asset resource.
- [class PHAssetResourceUploadJobChangeRequest](./phassetresourceuploadjobchangerequest.md)
  Use within an application’s `com.apple.photos.background-upload` extension to create and change [`PHAssetResourceUploadJob`](./phassetresourceuploadjob.md) records.
### Live Photos
- [class PHLivePhoto](./phlivephoto.md)
  A displayable representation of a Live Photo.
### Errors
- [struct PHPhotosError](./phphotoserror-swift.struct.md)
  A structure that represents a framework error.
- [let PHPhotosErrorDomain: String](./phphotoserrordomain.md)
  A string representation of the error domain.
### Deprecated errors
- [Deprecated Errors](../PhotoKit/deprecated-errors.md)
  Review unsupported errors and their replacements.
### Classes
- [class PHProject](./phproject.md)
  A representation of a Photos app project extension.
- [class PHProjectChangeRequest](./phprojectchangerequest.md)
  A request to change asset data in a Photos project extension.
- [class PHAssetResourceUploadJobOptions](./phassetresourceuploadjoboptions.md)
  Options that affect the service behavior when processing Asset Resource Upload Jobs.
- [class PHReferenceImageInfo](./phreferenceimageinfo.md)
### Protocols
- [protocol PHBackgroundResourceUploadJobExtension](./phbackgroundresourceuploadjobextension.md)
  A protocol to interact with asset resource upload jobs during background processing.
- [protocol PHPhotoLibraryPersistentChangesObserver](./phphotolibrarypersistentchangesobserver.md)
### Enumerations
- [PHAssetAdjustmentsState](./phasset/adjustmentsstate-swift.enum.md)
- [PHAssetPlaybackVariation](./phasset/playbackvariation-swift.enum.md)

## See Also

### Frameworks
- [PhotosUI](../PhotosUI/PhotosUI.md)
  Present a person’s photo library using a picker interface, display Live Photos, or extend the Photos app with custom functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos)*