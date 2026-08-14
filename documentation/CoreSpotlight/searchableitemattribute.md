# SearchableItemAttribute

**Framework**: Core Spotlight  
**Kind**: struct

An attribute from a content item that the Spotlight search tool can include in search results.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SearchableItemAttribute
```

#### Overview

When searching your content, the [`SpotlightSearchTool`](spotlightsearchtool.md) can retrieve attributes for found items in advance and include them with search results. When you configure a [`CoreSpotlightSource`](corespotlightsource.md) or [`FileSource`](filesource.md) for this tool, specify the attributes you want to retrieve from that source. The tool retrieves the attributes from any items and delivers them to the model as additional context to consider. If you don’t specify any attributes, the tool retrieves only the unique identifier of each search result.

## Topics

### Describing general attributes
- [static let alternateNames: SearchableItemAttribute](searchableitemattribute/alternatenames.md)
- [static let contentType: SearchableItemAttribute](searchableitemattribute/contenttype.md)
- [static let contentTypeTree: SearchableItemAttribute](searchableitemattribute/contenttypetree.md)
- [static let contentURL: SearchableItemAttribute](searchableitemattribute/contenturl.md)
- [static let darkThumbnailURL: SearchableItemAttribute](searchableitemattribute/darkthumbnailurl.md)
- [static let displayName: SearchableItemAttribute](searchableitemattribute/displayname.md)
- [static let keywords: SearchableItemAttribute](searchableitemattribute/keywords.md)
- [static let metadataModificationDate: SearchableItemAttribute](searchableitemattribute/metadatamodificationdate.md)
- [static let path: SearchableItemAttribute](searchableitemattribute/path.md)
- [static let rankingHint: SearchableItemAttribute](searchableitemattribute/rankinghint.md)
- [static let relatedUniqueIdentifier: SearchableItemAttribute](searchableitemattribute/relateduniqueidentifier.md)
- [static let thumbnailData: SearchableItemAttribute](searchableitemattribute/thumbnaildata.md)
- [static let thumbnailURL: SearchableItemAttribute](searchableitemattribute/thumbnailurl.md)
- [static let title: SearchableItemAttribute](searchableitemattribute/title.md)
- [static let domainIdentifier: SearchableItemAttribute](searchableitemattribute/domainidentifier.md)
- [static let weakRelatedUniqueIdentifier: SearchableItemAttribute](searchableitemattribute/weakrelateduniqueidentifier.md)
### Describing document content
- [static let audiences: SearchableItemAttribute](searchableitemattribute/audiences.md)
- [static let contentDescription: SearchableItemAttribute](searchableitemattribute/contentdescription.md)
- [static let creator: SearchableItemAttribute](searchableitemattribute/creator.md)
- [static let encodingApplications: SearchableItemAttribute](searchableitemattribute/encodingapplications.md)
- [static let fileSize: SearchableItemAttribute](searchableitemattribute/filesize.md)
- [static let fontNames: SearchableItemAttribute](searchableitemattribute/fontnames.md)
- [static let identifier: SearchableItemAttribute](searchableitemattribute/identifier.md)
- [static let kind: SearchableItemAttribute](searchableitemattribute/kind.md)
- [static let pageCount: SearchableItemAttribute](searchableitemattribute/pagecount.md)
- [static let pageHeight: SearchableItemAttribute](searchableitemattribute/pageheight.md)
- [static let pageWidth: SearchableItemAttribute](searchableitemattribute/pagewidth.md)
- [static let securityMethod: SearchableItemAttribute](searchableitemattribute/securitymethod.md)
- [static let subject: SearchableItemAttribute](searchableitemattribute/subject.md)
- [static let theme: SearchableItemAttribute](searchableitemattribute/theme.md)
### Describing user involvement
- [static let userCreated: SearchableItemAttribute](searchableitemattribute/usercreated.md)
- [static let userCurated: SearchableItemAttribute](searchableitemattribute/usercurated.md)
- [static let userOwned: SearchableItemAttribute](searchableitemattribute/userowned.md)
### Describing events
- [static let allDay: SearchableItemAttribute](searchableitemattribute/allday.md)
- [static let completionDate: SearchableItemAttribute](searchableitemattribute/completiondate.md)
- [static let dueDate: SearchableItemAttribute](searchableitemattribute/duedate.md)
- [static let endDate: SearchableItemAttribute](searchableitemattribute/enddate.md)
- [static let importantDates: SearchableItemAttribute](searchableitemattribute/importantdates.md)
- [static let startDate: SearchableItemAttribute](searchableitemattribute/startdate.md)
### Describing places
- [static let altitude: SearchableItemAttribute](searchableitemattribute/altitude.md)
- [static let city: SearchableItemAttribute](searchableitemattribute/city.md)
- [static let country: SearchableItemAttribute](searchableitemattribute/country.md)
- [static let gpsAreaInformation: SearchableItemAttribute](searchableitemattribute/gpsareainformation.md)
- [static let gpsDateStamp: SearchableItemAttribute](searchableitemattribute/gpsdatestamp.md)
- [static let gpsDestinationBearing: SearchableItemAttribute](searchableitemattribute/gpsdestinationbearing.md)
- [static let gpsDestinationDistance: SearchableItemAttribute](searchableitemattribute/gpsdestinationdistance.md)
- [static let gpsDestinationLatitude: SearchableItemAttribute](searchableitemattribute/gpsdestinationlatitude.md)
- [static let gpsDestinationLongitude: SearchableItemAttribute](searchableitemattribute/gpsdestinationlongitude.md)
- [static let gpsDifferential: SearchableItemAttribute](searchableitemattribute/gpsdifferential.md)
- [static let gpsDilutionOfPrecision: SearchableItemAttribute](searchableitemattribute/gpsdilutionofprecision.md)
- [static let gpsMapDatum: SearchableItemAttribute](searchableitemattribute/gpsmapdatum.md)
- [static let gpsMeasureMode: SearchableItemAttribute](searchableitemattribute/gpsmeasuremode.md)
- [static let gpsProcessingMethod: SearchableItemAttribute](searchableitemattribute/gpsprocessingmethod.md)
- [static let gpsStatus: SearchableItemAttribute](searchableitemattribute/gpsstatus.md)
- [static let gpsTrack: SearchableItemAttribute](searchableitemattribute/gpstrack.md)
- [static let headline: SearchableItemAttribute](searchableitemattribute/headline.md)
- [static let imageDirection: SearchableItemAttribute](searchableitemattribute/imagedirection.md)
- [static let instructions: SearchableItemAttribute](searchableitemattribute/instructions.md)
- [static let latitude: SearchableItemAttribute](searchableitemattribute/latitude.md)
- [static let longitude: SearchableItemAttribute](searchableitemattribute/longitude.md)
- [static let namedLocation: SearchableItemAttribute](searchableitemattribute/namedlocation.md)
- [static let speed: SearchableItemAttribute](searchableitemattribute/speed.md)
- [static let stateOrProvince: SearchableItemAttribute](searchableitemattribute/stateorprovince.md)
- [static let timestamp: SearchableItemAttribute](searchableitemattribute/timestamp.md)
- [static let fullyFormattedAddress: SearchableItemAttribute](searchableitemattribute/fullyformattedaddress.md)
- [static let postalCode: SearchableItemAttribute](searchableitemattribute/postalcode.md)
- [static let subThoroughfare: SearchableItemAttribute](searchableitemattribute/subthoroughfare.md)
- [static let thoroughfare: SearchableItemAttribute](searchableitemattribute/thoroughfare.md)
### Describing media
- [static let comment: SearchableItemAttribute](searchableitemattribute/comment.md)
- [static let contentCreationDate: SearchableItemAttribute](searchableitemattribute/contentcreationdate.md)
- [static let contentModificationDate: SearchableItemAttribute](searchableitemattribute/contentmodificationdate.md)
- [static let contentSources: SearchableItemAttribute](searchableitemattribute/contentsources.md)
- [static let copyright: SearchableItemAttribute](searchableitemattribute/copyright.md)
- [static let downloadedDate: SearchableItemAttribute](searchableitemattribute/downloadeddate.md)
- [static let editors: SearchableItemAttribute](searchableitemattribute/editors.md)
- [static let lastUsedDate: SearchableItemAttribute](searchableitemattribute/lastuseddate.md)
- [static let participants: SearchableItemAttribute](searchableitemattribute/participants.md)
- [static let projects: SearchableItemAttribute](searchableitemattribute/projects.md)
- [static let addedDate: SearchableItemAttribute](searchableitemattribute/addeddate.md)
- [static let codecs: SearchableItemAttribute](searchableitemattribute/codecs.md)
- [static let contactKeywords: SearchableItemAttribute](searchableitemattribute/contactkeywords.md)
- [static let deliveryType: SearchableItemAttribute](searchableitemattribute/deliverytype.md)
- [static let duration: SearchableItemAttribute](searchableitemattribute/duration.md)
- [static let mediaTypes: SearchableItemAttribute](searchableitemattribute/mediatypes.md)
- [static let organizations: SearchableItemAttribute](searchableitemattribute/organizations.md)
- [static let streamable: SearchableItemAttribute](searchableitemattribute/streamable.md)
- [static let totalBitRate: SearchableItemAttribute](searchableitemattribute/totalbitrate.md)
- [static let audioBitRate: SearchableItemAttribute](searchableitemattribute/audiobitrate.md)
- [static let version: SearchableItemAttribute](searchableitemattribute/version.md)
- [static let videoBitRate: SearchableItemAttribute](searchableitemattribute/videobitrate.md)
- [static let contributors: SearchableItemAttribute](searchableitemattribute/contributors.md)
- [static let languages: SearchableItemAttribute](searchableitemattribute/languages.md)
- [static let publishers: SearchableItemAttribute](searchableitemattribute/publishers.md)
- [static let rights: SearchableItemAttribute](searchableitemattribute/rights.md)
- [static let role: SearchableItemAttribute](searchableitemattribute/role.md)
- [static let contentRating: SearchableItemAttribute](searchableitemattribute/contentrating.md)
- [static let coverage: SearchableItemAttribute](searchableitemattribute/coverage.md)
- [static let director: SearchableItemAttribute](searchableitemattribute/director.md)
- [static let genre: SearchableItemAttribute](searchableitemattribute/genre.md)
- [static let information: SearchableItemAttribute](searchableitemattribute/information.md)
- [static let local: SearchableItemAttribute](searchableitemattribute/local.md)
- [static let originalFormat: SearchableItemAttribute](searchableitemattribute/originalformat.md)
- [static let originalSource: SearchableItemAttribute](searchableitemattribute/originalsource.md)
- [static let performers: SearchableItemAttribute](searchableitemattribute/performers.md)
- [static let playCount: SearchableItemAttribute](searchableitemattribute/playcount.md)
- [static let producer: SearchableItemAttribute](searchableitemattribute/producer.md)
- [static let rating: SearchableItemAttribute](searchableitemattribute/rating.md)
- [static let ratingDescription: SearchableItemAttribute](searchableitemattribute/ratingdescription.md)
- [static let url: SearchableItemAttribute](searchableitemattribute/url.md)
### Describing music
- [static let album: SearchableItemAttribute](searchableitemattribute/album.md)
- [static let artist: SearchableItemAttribute](searchableitemattribute/artist.md)
- [static let audioChannelCount: SearchableItemAttribute](searchableitemattribute/audiochannelcount.md)
- [static let audioEncodingApplication: SearchableItemAttribute](searchableitemattribute/audioencodingapplication.md)
- [static let audioSampleRate: SearchableItemAttribute](searchableitemattribute/audiosamplerate.md)
- [static let audioTrackNumber: SearchableItemAttribute](searchableitemattribute/audiotracknumber.md)
- [static let composer: SearchableItemAttribute](searchableitemattribute/composer.md)
- [static let keySignature: SearchableItemAttribute](searchableitemattribute/keysignature.md)
- [static let lyricist: SearchableItemAttribute](searchableitemattribute/lyricist.md)
- [static let musicalGenre: SearchableItemAttribute](searchableitemattribute/musicalgenre.md)
- [static let recordingDate: SearchableItemAttribute](searchableitemattribute/recordingdate.md)
- [static let tempo: SearchableItemAttribute](searchableitemattribute/tempo.md)
- [static let timeSignature: SearchableItemAttribute](searchableitemattribute/timesignature.md)
- [static let generalMIDISequence: SearchableItemAttribute](searchableitemattribute/generalmidisequence.md)
- [static let musicalInstrumentCategory: SearchableItemAttribute](searchableitemattribute/musicalinstrumentcategory.md)
- [static let musicalInstrumentName: SearchableItemAttribute](searchableitemattribute/musicalinstrumentname.md)
### Describing images
- [static let isoSpeed: SearchableItemAttribute](searchableitemattribute/isospeed.md)
- [static let acquisitionMake: SearchableItemAttribute](searchableitemattribute/acquisitionmake.md)
- [static let acquisitionModel: SearchableItemAttribute](searchableitemattribute/acquisitionmodel.md)
- [static let aperture: SearchableItemAttribute](searchableitemattribute/aperture.md)
- [static let bitsPerSample: SearchableItemAttribute](searchableitemattribute/bitspersample.md)
- [static let cameraOwner: SearchableItemAttribute](searchableitemattribute/cameraowner.md)
- [static let colorSpace: SearchableItemAttribute](searchableitemattribute/colorspace.md)
- [static let flashOn: SearchableItemAttribute](searchableitemattribute/flashon.md)
- [static let focalLength: SearchableItemAttribute](searchableitemattribute/focallength.md)
- [static let focalLength35mmEquivalent: SearchableItemAttribute](searchableitemattribute/focallength35mmequivalent.md)
- [static let layerNames: SearchableItemAttribute](searchableitemattribute/layernames.md)
- [static let lensModel: SearchableItemAttribute](searchableitemattribute/lensmodel.md)
- [static let orientation: SearchableItemAttribute](searchableitemattribute/orientation.md)
- [static let pixelCount: SearchableItemAttribute](searchableitemattribute/pixelcount.md)
- [static let pixelHeight: SearchableItemAttribute](searchableitemattribute/pixelheight.md)
- [static let pixelWidth: SearchableItemAttribute](searchableitemattribute/pixelwidth.md)
- [static let whiteBalance: SearchableItemAttribute](searchableitemattribute/whitebalance.md)
- [static let exifGPSVersion: SearchableItemAttribute](searchableitemattribute/exifgpsversion.md)
- [static let exifVersion: SearchableItemAttribute](searchableitemattribute/exifversion.md)
- [static let exposureMode: SearchableItemAttribute](searchableitemattribute/exposuremode.md)
- [static let exposureProgram: SearchableItemAttribute](searchableitemattribute/exposureprogram.md)
- [static let exposureTime: SearchableItemAttribute](searchableitemattribute/exposuretime.md)
- [static let exposureTimeString: SearchableItemAttribute](searchableitemattribute/exposuretimestring.md)
- [static let fNumber: SearchableItemAttribute](searchableitemattribute/fnumber.md)
- [static let hasAlphaChannel: SearchableItemAttribute](searchableitemattribute/hasalphachannel.md)
- [static let maximumAperture: SearchableItemAttribute](searchableitemattribute/maximumaperture.md)
- [static let meteringMode: SearchableItemAttribute](searchableitemattribute/meteringmode.md)
- [static let profileName: SearchableItemAttribute](searchableitemattribute/profilename.md)
- [static let redEyeOn: SearchableItemAttribute](searchableitemattribute/redeyeon.md)
- [static let resolutionHeightDPI: SearchableItemAttribute](searchableitemattribute/resolutionheightdpi.md)
- [static let resolutionWidthDPI: SearchableItemAttribute](searchableitemattribute/resolutionwidthdpi.md)
### Describing messages
- [static let accountHandles: SearchableItemAttribute](searchableitemattribute/accounthandles.md)
- [static let accountIdentifier: SearchableItemAttribute](searchableitemattribute/accountidentifier.md)
- [static let authorAddresses: SearchableItemAttribute](searchableitemattribute/authoraddresses.md)
- [static let authorEmailAddresses: SearchableItemAttribute](searchableitemattribute/authoremailaddresses.md)
- [static let authorNames: SearchableItemAttribute](searchableitemattribute/authornames.md)
- [static let emailAddresses: SearchableItemAttribute](searchableitemattribute/emailaddresses.md)
- [static let instantMessageAddresses: SearchableItemAttribute](searchableitemattribute/instantmessageaddresses.md)
- [static let likelyJunk: SearchableItemAttribute](searchableitemattribute/likelyjunk.md)
- [static let mailboxIdentifiers: SearchableItemAttribute](searchableitemattribute/mailboxidentifiers.md)
- [static let phoneNumbers: SearchableItemAttribute](searchableitemattribute/phonenumbers.md)
- [static let recipientAddresses: SearchableItemAttribute](searchableitemattribute/recipientaddresses.md)
- [static let recipientEmailAddresses: SearchableItemAttribute](searchableitemattribute/recipientemailaddresses.md)
- [static let recipientNames: SearchableItemAttribute](searchableitemattribute/recipientnames.md)
- [static let textContent: SearchableItemAttribute](searchableitemattribute/textcontent.md)
### Describing containment
- [static let containerDisplayName: SearchableItemAttribute](searchableitemattribute/containerdisplayname.md)
- [static let containerIdentifier: SearchableItemAttribute](searchableitemattribute/containeridentifier.md)
- [static let containerOrder: SearchableItemAttribute](searchableitemattribute/containerorder.md)
- [static let containerTitle: SearchableItemAttribute](searchableitemattribute/containertitle.md)
### Describing supporting actions
- [static let supportsNavigation: SearchableItemAttribute](searchableitemattribute/supportsnavigation.md)
- [static let supportsPhoneCall: SearchableItemAttribute](searchableitemattribute/supportsphonecall.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct SearchSource](searchsource.md)
  A source of data for Spotlight to search.
- [struct CoreSpotlightSource](corespotlightsource.md)
  A search source that retrieves data from the app’s Spotlight index.
- [struct FileSource](filesource.md)
  A search source that retrieves indexed metadata from files and directories visible to Spotlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchableitemattribute)*