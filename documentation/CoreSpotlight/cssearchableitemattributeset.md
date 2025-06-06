# CSSearchableItemAttributeSet

**Framework**: Core Spotlight  
**Kind**: class

The detailed metadata for a searchable item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class CSSearchableItemAttributeSet
```

## Mentions

- [Adding your app’s content to Spotlight indexes](adding-your-app-s-content-to-spotlight-indexes.md)
- [Searching for information in your app](searching-for-information-in-your-app.md)

#### Overview

A `CSSearchableItemAttributeSet` contains an extensive set of attributes that describe your app’s content. Attributes include information such as its title and a brief description. They can also refer to who created the item, what kind of data it represents, when someone created it, and more. During the indexing process, you create [`CSSearchableItem`](cssearchableitem.md) objects and use a `CSSearchableItemAttributeSet` to fill in the attributes for that item. During a search, you can query the index for items with attributes that match specific values.

When creating a [`CSSearchableItem`](cssearchableitem.md), it’s important to fill out as much information in the accompanying `CSSearchableItemAttributeSet` object as possible. You don’t have to provide values for every attribute. Instead, choose attributes that match the domain of your content. This type divides attributes into groups such as media, documents, events, places, music, images, and more. You can also add custom attributes to describe new types of content. When defining custom attributes, be as specific as possible in your definition, and provide a value for the [`contentTypeTree`](cssearchableitemattributeset/contenttypetree.md) property so your custom attribute inherits from a known type.

> ❗ **Important**: Modify a `CSSearchableItemAttributeSet` object on only one thread at a time. Concurrent access to properties in an attribute set has undefined behavior.

Modify a `CSSearchableItemAttributeSet` object on only one thread at a time. Concurrent access to properties in an attribute set has undefined behavior.

## Topics

### Getting an attribute set
- [init(contentType: UTType)](cssearchableitemattributeset/init(contenttype:).md)
  Creates an attribute set for the specified content type.
### Working with custom attributes
- [func setValue((any NSSecureCoding)?, forCustomKey: CSCustomAttributeKey)](cssearchableitemattributeset/setvalue(_:forcustomkey:).md)
  Sets the value for a custom attribute key.
- [func value(forCustomKey: CSCustomAttributeKey) -> (any NSSecureCoding)?](cssearchableitemattributeset/value(forcustomkey:).md)
  Returns the value associated with the specified custom attribute key.
### Describing Apple Intelligence prioritization and summarization
- [var isPriority: NSNumber?](cssearchableitemattributeset/ispriority.md)
  A Boolean value that indicates whether the mail or messages content represents a prioritized item.
- [var textContentSummary: String?](cssearchableitemattributeset/textcontentsummary.md)
  A string that presents the Apple Intelligence summarization of the item.
- [var transcribedTextContent: String?](cssearchableitemattributeset/transcribedtextcontent.md)
  A string that represents the text the system transcribed.
### Describing documents
- [var audiences: [String]?](cssearchableitemattributeset/audiences.md)
  A class of entity for which the item is intended or useful.
- [var contentDescription: String?](cssearchableitemattributeset/contentdescription.md)
  A description of the item’s content.
- [var creator: String?](cssearchableitemattributeset/creator.md)
  The name of the app that created the content.
- [var encodingApplications: [String]?](cssearchableitemattributeset/encodingapplications.md)
  The name of the apps that converted the original content into a PDF stream.
- [var fileSize: NSNumber?](cssearchableitemattributeset/filesize.md)
  The size of the document file.
- [var fontNames: [String]?](cssearchableitemattributeset/fontnames.md)
  An array of font names the document uses.
- [var identifier: String?](cssearchableitemattributeset/identifier.md)
  A formal identifier that references the document the item represents.
- [var kind: String?](cssearchableitemattributeset/kind.md)
  A description of the kind of document the item represents.
- [var pageCount: NSNumber?](cssearchableitemattributeset/pagecount.md)
  The number of pages in the document.
- [var pageHeight: NSNumber?](cssearchableitemattributeset/pageheight.md)
  The height of the document page, in points (72 points per inch).
- [var pageWidth: NSNumber?](cssearchableitemattributeset/pagewidth.md)
  The width of the document page, in points (72 points per inch).
- [var securityMethod: String?](cssearchableitemattributeset/securitymethod.md)
  The security method (a type of encryption) that protects the document file.
- [var subject: String?](cssearchableitemattributeset/subject.md)
  The subject of the document.
- [var theme: String?](cssearchableitemattributeset/theme.md)
  The theme of the document.
### Describing general attributes
- [var alternateNames: [String]?](cssearchableitemattributeset/alternatenames.md)
  An array of localized strings that represent alternate display names for the item.
- [var contentType: String?](cssearchableitemattributeset/contenttype.md)
  The uniform type identifier (UTI) of the item.
- [var contentTypeTree: [String]?](cssearchableitemattributeset/contenttypetree.md)
  An attribute type that identifies a custom hierarchy of types to describe the attributes of your item.
- [var contentURL: URL?](cssearchableitemattributeset/contenturl.md)
  The file URL of the content to index.
- [var darkThumbnailURL: URL?](cssearchableitemattributeset/darkthumbnailurl.md)
  The local file URL of the thumbnail image for the item when Dark Mode is active.
- [var displayName: String?](cssearchableitemattributeset/displayname.md)
  A localized string that contains the name of the item, suitable to display in the user interface.
- [var keywords: [String]?](cssearchableitemattributeset/keywords.md)
  An array of keywords associated with the item, such as work, birthday, important, and so on.
- [var metadataModificationDate: Date?](cssearchableitemattributeset/metadatamodificationdate.md)
  The date on which the last metadata attribute was changed.
- [var path: String?](cssearchableitemattributeset/path.md)
  The complete path to the item.
- [var rankingHint: NSNumber?](cssearchableitemattributeset/rankinghint.md)
  A number that indicates the relative importance of the item among other items from the app.
- [var relatedUniqueIdentifier: String?](cssearchableitemattributeset/relateduniqueidentifier.md)
  The unique identifier for the item to which the activity is related.
- [var thumbnailData: Data?](cssearchableitemattributeset/thumbnaildata.md)
  Image data that represents the thumbnail of the item.
- [var thumbnailURL: URL?](cssearchableitemattributeset/thumbnailurl.md)
  The local file URL of the thumbnail image for the item.
- [var title: String?](cssearchableitemattributeset/title.md)
  The title of the item.
- [var domainIdentifier: String?](cssearchableitemattributeset/domainidentifier.md)
  An identifier that represents the domain or owner of the item.
- [var weakRelatedUniqueIdentifier: String?](cssearchableitemattributeset/weakrelateduniqueidentifier.md)
  The unique identifier for the item to which the activity is related, but not linked.
### Describing user involvement
- [var userCreated: NSNumber?](cssearchableitemattributeset/usercreated.md)
  A value that indicates the user created the item.
- [var userCurated: NSNumber?](cssearchableitemattributeset/usercurated.md)
  A value that indicates the user selected the item.
- [var userOwned: NSNumber?](cssearchableitemattributeset/userowned.md)
  A value that indicates the user purchased or owns the item.
### Describing events
- [var allDay: NSNumber?](cssearchableitemattributeset/allday.md)
  A value that indicates if the event covers an entire day.
- [var completionDate: Date?](cssearchableitemattributeset/completiondate.md)
  The date on which the item was completed.
- [var dueDate: Date?](cssearchableitemattributeset/duedate.md)
  The date on which the item is due.
- [var endDate: Date?](cssearchableitemattributeset/enddate.md)
  The end date for the item.
- [var importantDates: [Date]?](cssearchableitemattributeset/importantdates.md)
  An array of important dates associated with the item.
- [var startDate: Date?](cssearchableitemattributeset/startdate.md)
  The start date for the item.
### Describing places
- [var altitude: NSNumber?](cssearchableitemattributeset/altitude.md)
  The altitude of the item in meters above sea level, expressed using the WGS84 datum.
- [var city: String?](cssearchableitemattributeset/city.md)
  The city of the item’s origin according to guidelines that the provider establishes.
- [var country: String?](cssearchableitemattributeset/country.md)
  The full, publishable name of the country or region in which the intellectual property of the item was created, according to guidelines the provider establishes.
- [var gpsAreaInformation: String?](cssearchableitemattributeset/gpsareainformation.md)
  Information about the GPS area.
- [var gpsdop: NSNumber?](cssearchableitemattributeset/gpsdop.md)
  The GPS dilution of precision value.
- [var gpsDateStamp: Date?](cssearchableitemattributeset/gpsdatestamp.md)
  The date and time related to the GPS value.
- [var gpsDestBearing: NSNumber?](cssearchableitemattributeset/gpsdestbearing.md)
  The bearing to the destination point.
- [var gpsDestDistance: NSNumber?](cssearchableitemattributeset/gpsdestdistance.md)
  The distance to the destination point.
- [var gpsDestLatitude: NSNumber?](cssearchableitemattributeset/gpsdestlatitude.md)
  The latitude of the destination point.
- [var gpsDestLongitude: NSNumber?](cssearchableitemattributeset/gpsdestlongitude.md)
  The longitude of the destination point.
- [var gpsDifferental: NSNumber?](cssearchableitemattributeset/gpsdifferental.md)
  The differential correction applied to the GPS receiver.
- [var gpsMapDatum: String?](cssearchableitemattributeset/gpsmapdatum.md)
  The geodetic data that the GPS receiver uses.
- [var gpsMeasureMode: String?](cssearchableitemattributeset/gpsmeasuremode.md)
  The measurement precision mode in use by the GPS receiver.
- [var gpsProcessingMethod: String?](cssearchableitemattributeset/gpsprocessingmethod.md)
  The location finding method that the GPS receiver uses.
- [var gpsStatus: String?](cssearchableitemattributeset/gpsstatus.md)
  The status of the GPS receiver.
- [var gpsTrack: NSNumber?](cssearchableitemattributeset/gpstrack.md)
  The direction of travel of the item in degrees from true north.
- [var headline: String?](cssearchableitemattributeset/headline.md)
  A publishable string that provides a synopsis of the contents of the item.
- [var imageDirection: NSNumber?](cssearchableitemattributeset/imagedirection.md)
  The direction of the item’s image in degrees from true north.
- [var instructions: String?](cssearchableitemattributeset/instructions.md)
  Instructions that concern the use of the item, such as an embargo or warning.
- [var latitude: NSNumber?](cssearchableitemattributeset/latitude.md)
  The latitude of the item, in degrees north of the equator, expressed using the WGS84 datum.
- [var longitude: NSNumber?](cssearchableitemattributeset/longitude.md)
  The longitude of the item, in degrees east of the prime meridian, expressed using the WGS84 datum.
- [var namedLocation: String?](cssearchableitemattributeset/namedlocation.md)
  The name of the location or point of interest associated with the item.
- [var speed: NSNumber?](cssearchableitemattributeset/speed.md)
  The speed of the item, in kilometers per hour.
- [var stateOrProvince: String?](cssearchableitemattributeset/stateorprovince.md)
  The province or state of origin according to guidelines the provider establishes.
- [var timestamp: Date?](cssearchableitemattributeset/timestamp.md)
  The timestamp on the item.
- [var fullyFormattedAddress: String?](cssearchableitemattributeset/fullyformattedaddress.md)
  The fully formatted address of the item, received from MapKit.
- [var postalCode: String?](cssearchableitemattributeset/postalcode.md)
  The postal code for the item according to guidelines the provider establishes.
- [var subThoroughfare: String?](cssearchableitemattributeset/subthoroughfare.md)
  The sublocation, such as a street number, for the item according to guidelines the provider establishes.
- [var thoroughfare: String?](cssearchableitemattributeset/thoroughfare.md)
  The thoroughfare, such as a street name, associated with the location for the item according to guidelines the provider establishes.
### Describing media
- [var comment: String?](cssearchableitemattributeset/comment.md)
  A comment related to the media file.
- [var contentCreationDate: Date?](cssearchableitemattributeset/contentcreationdate.md)
  The creation date of an edited or optimized version of the song or composition.
- [var contentModificationDate: Date?](cssearchableitemattributeset/contentmodificationdate.md)
  The date on which the contents of the file was last modified.
- [var contentSources: [String]?](cssearchableitemattributeset/contentsources.md)
  An array of sources from which the media was obtained.
- [var copyright: String?](cssearchableitemattributeset/copyright.md)
  The copyright date of the content.
- [var downloadedDate: Date?](cssearchableitemattributeset/downloadeddate.md)
  The most recent date on which the file was downloaded or received.
- [var editors: [String]?](cssearchableitemattributeset/editors.md)
  A list of editors who have worked on the file.
- [var lastUsedDate: Date?](cssearchableitemattributeset/lastuseddate.md)
  The date on which the file was last used.
- [var participants: [String]?](cssearchableitemattributeset/participants.md)
  A list of people who are visible in an image or movie or written about in a document.
- [var projects: [String]?](cssearchableitemattributeset/projects.md)
  A list of projects of which this file is a part.
- [var addedDate: Date?](cssearchableitemattributeset/addeddate.md)
  The date on which the item was moved into its current location.
- [var codecs: [String]?](cssearchableitemattributeset/codecs.md)
  The codecs used to encode/decode the media.
- [var contactKeywords: [String]?](cssearchableitemattributeset/contactkeywords.md)
  A list of contacts who are associated with the content in some way, not including the author.
- [var deliveryType: NSNumber?](cssearchableitemattributeset/deliverytype.md)
  The delivery type of the file.
- [var duration: NSNumber?](cssearchableitemattributeset/duration.md)
  The duration (if appropriate) of the content of the file, in seconds.
- [var mediaTypes: [String]?](cssearchableitemattributeset/mediatypes.md)
  The media types present in the content.
- [var organizations: [String]?](cssearchableitemattributeset/organizations.md)
  A list of companies or organizations that created the content.
- [var streamable: NSNumber?](cssearchableitemattributeset/streamable.md)
  A value that indicates if the content is prepared for streaming.
- [var totalBitRate: NSNumber?](cssearchableitemattributeset/totalbitrate.md)
  The total bit rate of the media, combining audio and video.
- [var audioBitRate: NSNumber?](cssearchableitemattributeset/audiobitrate.md)
  The audio bit rate of the media.
- [var version: String?](cssearchableitemattributeset/version.md)
  A version string associated with the file.
- [var videoBitRate: NSNumber?](cssearchableitemattributeset/videobitrate.md)
  The video bit rate of the media.
- [var contributors: [String]?](cssearchableitemattributeset/contributors.md)
  A list of people, organizations, or services that made contributions to the media content.
- [var languages: [String]?](cssearchableitemattributeset/languages.md)
  A list of the included languages for the intellectual content of the media.
- [var publishers: [String]?](cssearchableitemattributeset/publishers.md)
  A list of people, organizations, services, or other entities responsible for making the media available.
- [var rights: String?](cssearchableitemattributeset/rights.md)
  A link to information about the rights held in and over the media.
- [var role: String?](cssearchableitemattributeset/role.md)
  Indicates the role of the content creator.
- [var contentRating: NSNumber?](cssearchableitemattributeset/contentrating.md)
  A value that indicates if the media contains explicit content.
- [var coverage: [String]?](cssearchableitemattributeset/coverage.md)
  A list of descriptors that specify the extent or scope of the media.
- [var director: String?](cssearchableitemattributeset/director.md)
  The name of the director of the media (for example, a movie director).
- [var genre: String?](cssearchableitemattributeset/genre.md)
  The genre of the media.
- [var information: String?](cssearchableitemattributeset/information.md)
  Information about the media.
- [var local: NSNumber?](cssearchableitemattributeset/local.md)
  A value that indicates if the media is local.
- [var originalFormat: String?](cssearchableitemattributeset/originalformat.md)
  The original format of the media.
- [var originalSource: String?](cssearchableitemattributeset/originalsource.md)
  The original source of the media.
- [var performers: [String]?](cssearchableitemattributeset/performers.md)
  A list of performers in the media.
- [var playCount: NSNumber?](cssearchableitemattributeset/playcount.md)
  A user-supplied play count for the media.
- [var producer: String?](cssearchableitemattributeset/producer.md)
  The producer of the content.
- [var rating: NSNumber?](cssearchableitemattributeset/rating.md)
  The user-supplied rating of the media.
- [var ratingDescription: String?](cssearchableitemattributeset/ratingdescription.md)
  A description of the rating.
- [var url: URL?](cssearchableitemattributeset/url.md)
  The URL associated with the media.
### Describing music
- [var album: String?](cssearchableitemattributeset/album.md)
  The title for a collection of audio media.
- [var artist: String?](cssearchableitemattributeset/artist.md)
  The artist associated with the media.
- [var audioChannelCount: NSNumber?](cssearchableitemattributeset/audiochannelcount.md)
  The number of channels in the audio data that the file contains.
- [var audioEncodingApplication: String?](cssearchableitemattributeset/audioencodingapplication.md)
  The name of the application that encoded the data the audio file contains.
- [var audioSampleRate: NSNumber?](cssearchableitemattributeset/audiosamplerate.md)
  The sample rate of the audio data the file contains, as a float value representing Hz (audio frames per second), such as 44100.0 or 22254.54.
- [var audioTrackNumber: NSNumber?](cssearchableitemattributeset/audiotracknumber.md)
  The track number of a song or audio composition when part of an album.
- [var composer: String?](cssearchableitemattributeset/composer.md)
  The composer of the song or audio composition that the audio file contains.
- [var keySignature: String?](cssearchableitemattributeset/keysignature.md)
  The musical key of the song or audio composition that the file contains, such as C, Dm, or F#m.
- [var lyricist: String?](cssearchableitemattributeset/lyricist.md)
  The lyricist or text writer for the song or audio composition that the file contains.
- [var musicalGenre: String?](cssearchableitemattributeset/musicalgenre.md)
  The musical genre of the song or audio composition that the file contains, such as jazz, pop, rock, or classical.
- [var recordingDate: Date?](cssearchableitemattributeset/recordingdate.md)
  The recording date of the song or composition.
- [var tempo: NSNumber?](cssearchableitemattributeset/tempo.md)
  The tempo of the music that the audio file contains, in beats per minute.
- [var timeSignature: String?](cssearchableitemattributeset/timesignature.md)
  The time signature of the musical composition that the audio or MIDI file contains, in a string, such as “4/4” or “7/8”.
- [var generalMIDISequence: NSNumber?](cssearchableitemattributeset/generalmidisequence.md)
  A value that indicates whether the MIDI sequence the file contains is set up for use with a general MIDI device.
- [var musicalInstrumentCategory: String?](cssearchableitemattributeset/musicalinstrumentcategory.md)
  The category of the instrument associated with the audio file.
- [var musicalInstrumentName: String?](cssearchableitemattributeset/musicalinstrumentname.md)
  The name of an instrument within the context of an instrument category.
### Describing images
- [var isoSpeed: NSNumber?](cssearchableitemattributeset/isospeed.md)
  The ISO speed setting at the time the camera captured the image.
- [var acquisitionMake: String?](cssearchableitemattributeset/acquisitionmake.md)
  The manufacturer of the device that captured the image.
- [var acquisitionModel: String?](cssearchableitemattributeset/acquisitionmodel.md)
  The model of the device that captured the image.
- [var aperture: NSNumber?](cssearchableitemattributeset/aperture.md)
  The size of the lens aperture at the time the camera captured the image, as a log-scale APEX value.
- [var bitsPerSample: NSNumber?](cssearchableitemattributeset/bitspersample.md)
  The number of bits per sample.
- [var cameraOwner: String?](cssearchableitemattributeset/cameraowner.md)
  The owner of the camera that captured the image.
- [var colorSpace: String?](cssearchableitemattributeset/colorspace.md)
  The color space model the image uses, such as RGB, CMYK, YUV, or YCbCr.
- [var flashOn: NSNumber?](cssearchableitemattributeset/flashon.md)
  A value that indicates if the camera used a flash to capture the image.
- [var focalLength: NSNumber?](cssearchableitemattributeset/focallength.md)
  The actual focal length of the lens, in millimeters.
- [var focalLength35mm: NSNumber?](cssearchableitemattributeset/focallength35mm.md)
  A value that indicates if the focal length is 35mm.
- [var layerNames: [String]?](cssearchableitemattributeset/layernames.md)
  An array that contains the names of the various layers in the file.
- [var lensModel: String?](cssearchableitemattributeset/lensmodel.md)
  The model of the lens that captured the image.
- [var orientation: NSNumber?](cssearchableitemattributeset/orientation.md)
  The orientation of the data.
- [var pixelCount: NSNumber?](cssearchableitemattributeset/pixelcount.md)
  The total number of pixels in the image.
- [var pixelHeight: NSNumber?](cssearchableitemattributeset/pixelheight.md)
  The height of the item, such as image or video frame height, in pixels.
- [var pixelWidth: NSNumber?](cssearchableitemattributeset/pixelwidth.md)
  The width of the item, such as image or video frame width, in pixels.
- [var whiteBalance: NSNumber?](cssearchableitemattributeset/whitebalance.md)
  The white balance setting when the camera captured the image.
- [var exifgpsVersion: String?](cssearchableitemattributeset/exifgpsversion.md)
  The version of GPS Info IFD header that was used to generate the metadata for the image.
- [var exifVersion: String?](cssearchableitemattributeset/exifversion.md)
  The version of the EXIF header that was used to generate the metadata for the image.
- [var exposureMode: NSNumber?](cssearchableitemattributeset/exposuremode.md)
  The mode the camera used for the exposure of the image.
- [var exposureProgram: String?](cssearchableitemattributeset/exposureprogram.md)
  The class of the program the camera used to set exposure when capturing the image.
- [var exposureTime: NSNumber?](cssearchableitemattributeset/exposuretime.md)
  The time that the lens was open during exposure, in seconds.
- [var exposureTimeString: String?](cssearchableitemattributeset/exposuretimestring.md)
  The time that the lens was open during exposure, in a string, such as “1/250 seconds”.
- [var fNumber: NSNumber?](cssearchableitemattributeset/fnumber.md)
  The focal length of the lens, divided by the diameter of the aperture when the camera captured the image.
- [var hasAlphaChannel: NSNumber?](cssearchableitemattributeset/hasalphachannel.md)
  Indicates if the image file has an alpha channel.
- [var maxAperture: NSNumber?](cssearchableitemattributeset/maxaperture.md)
  The smallest F number of the lens.
- [var meteringMode: String?](cssearchableitemattributeset/meteringmode.md)
  The metering mode.
- [var profileName: String?](cssearchableitemattributeset/profilename.md)
  The name of the color profile the camera used for the image.
- [var redEyeOn: NSNumber?](cssearchableitemattributeset/redeyeon.md)
  A value that indicates if the camera used red-eye reduction when capturing the image.
- [var resolutionHeightDPI: NSNumber?](cssearchableitemattributeset/resolutionheightdpi.md)
  The resolution height of the image, in DPI.
- [var resolutionWidthDPI: NSNumber?](cssearchableitemattributeset/resolutionwidthdpi.md)
  The resolution width of the image, in DPI.
### Describing messages
- [Common Mailbox Identifiers](common-mailbox-identifiers.md)
  Constants that describe common mailbox names.
- [var htmlContentData: Data?](cssearchableitemattributeset/htmlcontentdata.md)
  The HTML content of the document encoded as an NSData object representing a UTF-8 encoded string.
- [var accountHandles: [String]?](cssearchableitemattributeset/accounthandles.md)
  An array of the canonical handles for the account with which the message is associated.
- [var accountIdentifier: String?](cssearchableitemattributeset/accountidentifier.md)
  The unique identifier for the account with which the message is associated, if any.
- [var additionalRecipients: [CSPerson]?](cssearchableitemattributeset/additionalrecipients.md)
  An array of [`CSPerson`](csperson.md) objects representing the content of the Cc: field in an email message.
- [var authorAddresses: [String]?](cssearchableitemattributeset/authoraddresses.md)
  An array of addresses associated with the author of the message.
- [var authorEmailAddresses: [String]?](cssearchableitemattributeset/authoremailaddresses.md)
  An array of email addresses associated with the author of the message.
- [var authorNames: [String]?](cssearchableitemattributeset/authornames.md)
  An array of names representing the authors who have worked on the message.
- [var authors: [CSPerson]?](cssearchableitemattributeset/authors.md)
  An array of [`CSPerson`](csperson.md) objects representing the content of the From: field in an item.
- [var emailAddresses: [String]?](cssearchableitemattributeset/emailaddresses.md)
  An array of email addresses associated with the message.
- [var emailHeaders: [String : [Any]]?](cssearchableitemattributeset/emailheaders.md)
  A dictionary that contains all the headers of the message.
- [var hiddenAdditionalRecipients: [CSPerson]?](cssearchableitemattributeset/hiddenadditionalrecipients.md)
  An array of [`CSPerson`](csperson.md) objects representing the content of the Bcc: field in an email message.
- [var instantMessageAddresses: [String]?](cssearchableitemattributeset/instantmessageaddresses.md)
  An array of instant message addresses for the message.
- [var likelyJunk: NSNumber](cssearchableitemattributeset/likelyjunk.md)
  A value that indicates if the message is likely to be considered junk.
- [var mailboxIdentifiers: [String]?](cssearchableitemattributeset/mailboxidentifiers.md)
  An array of mailbox identifiers associated with the message.
- [var phoneNumbers: [String]?](cssearchableitemattributeset/phonenumbers.md)
  An array of phone numbers associated with the message.
- [var primaryRecipients: [CSPerson]?](cssearchableitemattributeset/primaryrecipients.md)
  An array of [`CSPerson`](csperson.md) objects representing the content of the To: field in an email message.
- [var recipientAddresses: [String]?](cssearchableitemattributeset/recipientaddresses.md)
  An array of addresses associated with the recipients of the message.
- [var recipientEmailAddresses: [String]?](cssearchableitemattributeset/recipientemailaddresses.md)
  An array of email addresses associated with the recipient.
- [var recipientNames: [String]?](cssearchableitemattributeset/recipientnames.md)
  An array of names representing the recipients of this message.
- [var textContent: String?](cssearchableitemattributeset/textcontent.md)
  The textual content of the message.
### Describing containment
- [var containerDisplayName: String?](cssearchableitemattributeset/containerdisplayname.md)
  A localized string that specifies the name of a container to which the item belongs, suitable to display in the user interface.
- [var containerIdentifier: String?](cssearchableitemattributeset/containeridentifier.md)
  The identifier of the container to which the item belongs.
- [var containerOrder: NSNumber?](cssearchableitemattributeset/containerorder.md)
  The order of the item within the container.
- [var containerTitle: String?](cssearchableitemattributeset/containertitle.md)
  The title of the container to which the item belongs.
### Supporting actions
- [var actionIdentifiers: [String]](cssearchableitemattributeset/actionidentifiers.md)
  The identifiers that specify custom actions the app supports for the item.
- [var supportsNavigation: NSNumber?](cssearchableitemattributeset/supportsnavigation.md)
  A value that indicates whether the item contains information sufficient to provide navigation to the location it represents.
- [var supportsPhoneCall: NSNumber?](cssearchableitemattributeset/supportsphonecall.md)
  A value that indicates whether the item contains information sufficient to allow a phone call to a number associated with the item.
- [var sharedItemContentType: UTType?](cssearchableitemattributeset/shareditemcontenttype.md)
  The file type of the item to enable the user to share items from Spotlight.
- [let CSActionIdentifier: String](csactionidentifier.md)
  A key that specifies the action’s identifier in a user activity.
### Providing item representations
- [var providerDataTypeIdentifiers: [String]?](cssearchableitemattributeset/providerdatatypeidentifiers.md)
  An array of identifiers that corresponds to data representations the delegate provides.
- [var providerFileTypeIdentifiers: [String]?](cssearchableitemattributeset/providerfiletypeidentifiers.md)
  An array of identifiers that corresponds to file representations the delegate provides.
- [var providerInPlaceFileTypeIdentifiers: [String]?](cssearchableitemattributeset/providerinplacefiletypeidentifiers.md)
  An array of identifiers that corresponds to in-place file representations the delegate provides.
### Deprecated
- [init(itemContentType: String)](cssearchableitemattributeset/init(itemcontenttype:).md)
  Creates an attribute set for the specified content type.
### Instance Methods
- [func associateAppEntity<Entity>(Entity, priority: Int)](cssearchableitemattributeset/associateappentity(_:priority:).md)
  Associates an app entity with this searchable item.
- [func move(from: CSSearchableItemAttributeSet)](cssearchableitemattributeset/move(from:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CSSearchableItem](cssearchableitem.md)
  The details of your app-specific content that someone might search for on their devices.
- [class CSCustomAttributeKey](cscustomattributekey.md)
  A key associated with a custom attribute for a searchable item.
- [class CSLocalizedString](cslocalizedstring.md)
  An object that displays localized text in search results related to your app.
- [class CSPerson](csperson.md)
  An object that represents a person in the context of search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset)*