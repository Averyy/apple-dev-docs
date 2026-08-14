# NSMetadataItem

**Framework**: Foundation  
**Kind**: class

The metadata associated with a file.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSMetadataItem
```

#### Overview

Metadata items provide a simple interface to retrieve the available attribute names and values.

## Topics

### Creating a Metadata Item
- [init?(url: URL)](nsmetadataitem/init(url:)-9xxs3.md)
  Initializes a metadata item with a given URL.
### Getting Item Attributes
- [var attributes: [String]](nsmetadataitem/attributes.md)
  An array containing the attribute keys for the metadata item’s values.
- [func value(forAttribute: String) -> Any?](nsmetadataitem/value(forattribute:).md)
  Returns the receiver’s metadata attribute name specified by a given key.
- [func values(forAttributes: [String]) -> [String : Any]?](nsmetadataitem/values(forattributes:).md)
  Returns a dictionary containing the key-value pairs for the attribute names specified by a given array of keys.
### Item Attribute Keys
- [let NSMetadataItemAudiencesKey: String](nsmetadataitemaudienceskey.md)
- [let NSMetadataItemAudioBitRateKey: String](nsmetadataitemaudiobitratekey.md)
- [let NSMetadataItemAudioChannelCountKey: String](nsmetadataitemaudiochannelcountkey.md)
- [let NSMetadataItemAudioEncodingApplicationKey: String](nsmetadataitemaudioencodingapplicationkey.md)
- [let NSMetadataItemAudioSampleRateKey: String](nsmetadataitemaudiosampleratekey.md)
- [let NSMetadataItemAudioTrackNumberKey: String](nsmetadataitemaudiotracknumberkey.md)
- [let NSMetadataItemAuthorAddressesKey: String](nsmetadataitemauthoraddresseskey.md)
- [let NSMetadataItemAuthorEmailAddressesKey: String](nsmetadataitemauthoremailaddresseskey.md)
- [let NSMetadataItemAuthorsKey: String](nsmetadataitemauthorskey.md)
- [let NSMetadataItemAcquisitionMakeKey: String](nsmetadataitemacquisitionmakekey.md)
- [let NSMetadataItemAcquisitionModelKey: String](nsmetadataitemacquisitionmodelkey.md)
- [let NSMetadataItemAlbumKey: String](nsmetadataitemalbumkey.md)
- [let NSMetadataItemAltitudeKey: String](nsmetadataitemaltitudekey.md)
- [let NSMetadataItemApertureKey: String](nsmetadataitemaperturekey.md)
- [let NSMetadataItemAppleLoopDescriptorsKey: String](nsmetadataitemappleloopdescriptorskey.md)
- [let NSMetadataItemAppleLoopsKeyFilterTypeKey: String](nsmetadataitemappleloopskeyfiltertypekey.md)
- [let NSMetadataItemAppleLoopsLoopModeKey: String](nsmetadataitemappleloopsloopmodekey.md)
- [let NSMetadataItemAppleLoopsRootKeyKey: String](nsmetadataitemappleloopsrootkeykey.md)
- [let NSMetadataItemApplicationCategoriesKey: String](nsmetadataitemapplicationcategorieskey.md)
- [let NSMetadataItemAttributeChangeDateKey: String](nsmetadataitemattributechangedatekey.md)
- [let NSMetadataItemFSNameKey: String](nsmetadataitemfsnamekey.md)
- [let NSMetadataItemDisplayNameKey: String](nsmetadataitemdisplaynamekey.md)
- [let NSMetadataItemURLKey: String](nsmetadataitemurlkey.md)
- [let NSMetadataItemPathKey: String](nsmetadataitempathkey.md)
- [let NSMetadataItemFSSizeKey: String](nsmetadataitemfssizekey.md)
- [let NSMetadataItemFSCreationDateKey: String](nsmetadataitemfscreationdatekey.md)
- [let NSMetadataItemFSContentChangeDateKey: String](nsmetadataitemfscontentchangedatekey.md)
- [let NSMetadataItemBitsPerSampleKey: String](nsmetadataitembitspersamplekey.md)
- [let NSMetadataItemCFBundleIdentifierKey: String](nsmetadataitemcfbundleidentifierkey.md)
- [let NSMetadataItemCameraOwnerKey: String](nsmetadataitemcameraownerkey.md)
- [let NSMetadataItemCityKey: String](nsmetadataitemcitykey.md)
- [let NSMetadataItemCodecsKey: String](nsmetadataitemcodecskey.md)
- [let NSMetadataItemColorSpaceKey: String](nsmetadataitemcolorspacekey.md)
- [let NSMetadataItemCommentKey: String](nsmetadataitemcommentkey.md)
- [let NSMetadataItemComposerKey: String](nsmetadataitemcomposerkey.md)
- [let NSMetadataItemContactKeywordsKey: String](nsmetadataitemcontactkeywordskey.md)
- [let NSMetadataItemContentCreationDateKey: String](nsmetadataitemcontentcreationdatekey.md)
- [let NSMetadataItemContentModificationDateKey: String](nsmetadataitemcontentmodificationdatekey.md)
- [let NSMetadataItemContentTypeKey: String](nsmetadataitemcontenttypekey.md)
  The content type (UTI) of the metadata item.
- [let NSMetadataItemContentTypeTreeKey: String](nsmetadataitemcontenttypetreekey.md)
  The content type tree of the metadata item.
- [let NSMetadataItemContributorsKey: String](nsmetadataitemcontributorskey.md)
- [let NSMetadataItemCopyrightKey: String](nsmetadataitemcopyrightkey.md)
- [let NSMetadataItemCountryKey: String](nsmetadataitemcountrykey.md)
- [let NSMetadataItemCoverageKey: String](nsmetadataitemcoveragekey.md)
- [let NSMetadataItemCreatorKey: String](nsmetadataitemcreatorkey.md)
- [let NSMetadataItemDateAddedKey: String](nsmetadataitemdateaddedkey.md)
- [let NSMetadataItemDeliveryTypeKey: String](nsmetadataitemdeliverytypekey.md)
- [let NSMetadataItemDescriptionKey: String](nsmetadataitemdescriptionkey.md)
- [let NSMetadataItemDirectorKey: String](nsmetadataitemdirectorkey.md)
- [let NSMetadataItemDownloadedDateKey: String](nsmetadataitemdownloadeddatekey.md)
- [let NSMetadataItemDueDateKey: String](nsmetadataitemduedatekey.md)
- [let NSMetadataItemDurationSecondsKey: String](nsmetadataitemdurationsecondskey.md)
- [let NSMetadataItemEXIFGPSVersionKey: String](nsmetadataitemexifgpsversionkey.md)
- [let NSMetadataItemEXIFVersionKey: String](nsmetadataitemexifversionkey.md)
- [let NSMetadataItemEditorsKey: String](nsmetadataitemeditorskey.md)
- [let NSMetadataItemEmailAddressesKey: String](nsmetadataitememailaddresseskey.md)
- [let NSMetadataItemEncodingApplicationsKey: String](nsmetadataitemencodingapplicationskey.md)
- [let NSMetadataItemExecutableArchitecturesKey: String](nsmetadataitemexecutablearchitectureskey.md)
- [let NSMetadataItemExecutablePlatformKey: String](nsmetadataitemexecutableplatformkey.md)
- [let NSMetadataItemExposureModeKey: String](nsmetadataitemexposuremodekey.md)
- [let NSMetadataItemExposureProgramKey: String](nsmetadataitemexposureprogramkey.md)
- [let NSMetadataItemExposureTimeSecondsKey: String](nsmetadataitemexposuretimesecondskey.md)
- [let NSMetadataItemExposureTimeStringKey: String](nsmetadataitemexposuretimestringkey.md)
- [let NSMetadataItemFNumberKey: String](nsmetadataitemfnumberkey.md)
- [let NSMetadataItemFinderCommentKey: String](nsmetadataitemfindercommentkey.md)
- [let NSMetadataItemFlashOnOffKey: String](nsmetadataitemflashonoffkey.md)
- [let NSMetadataItemFocalLength35mmKey: String](nsmetadataitemfocallength35mmkey.md)
- [let NSMetadataItemFocalLengthKey: String](nsmetadataitemfocallengthkey.md)
- [let NSMetadataItemFontsKey: String](nsmetadataitemfontskey.md)
- [let NSMetadataItemGPSAreaInformationKey: String](nsmetadataitemgpsareainformationkey.md)
- [let NSMetadataItemGPSDOPKey: String](nsmetadataitemgpsdopkey.md)
- [let NSMetadataItemGPSDateStampKey: String](nsmetadataitemgpsdatestampkey.md)
- [let NSMetadataItemGPSDestBearingKey: String](nsmetadataitemgpsdestbearingkey.md)
- [let NSMetadataItemGPSDestDistanceKey: String](nsmetadataitemgpsdestdistancekey.md)
- [let NSMetadataItemGPSDestLatitudeKey: String](nsmetadataitemgpsdestlatitudekey.md)
- [let NSMetadataItemGPSDestLongitudeKey: String](nsmetadataitemgpsdestlongitudekey.md)
- [let NSMetadataItemGPSDifferentalKey: String](nsmetadataitemgpsdifferentalkey.md)
- [let NSMetadataItemGPSMapDatumKey: String](nsmetadataitemgpsmapdatumkey.md)
- [let NSMetadataItemGPSMeasureModeKey: String](nsmetadataitemgpsmeasuremodekey.md)
- [let NSMetadataItemGPSProcessingMethodKey: String](nsmetadataitemgpsprocessingmethodkey.md)
- [let NSMetadataItemGPSStatusKey: String](nsmetadataitemgpsstatuskey.md)
- [let NSMetadataItemGPSTrackKey: String](nsmetadataitemgpstrackkey.md)
- [let NSMetadataItemGenreKey: String](nsmetadataitemgenrekey.md)
- [let NSMetadataItemHasAlphaChannelKey: String](nsmetadataitemhasalphachannelkey.md)
- [let NSMetadataItemHeadlineKey: String](nsmetadataitemheadlinekey.md)
- [let NSMetadataItemISOSpeedKey: String](nsmetadataitemisospeedkey.md)
- [let NSMetadataItemIdentifierKey: String](nsmetadataitemidentifierkey.md)
- [let NSMetadataItemImageDirectionKey: String](nsmetadataitemimagedirectionkey.md)
- [let NSMetadataItemInformationKey: String](nsmetadataiteminformationkey.md)
- [let NSMetadataItemInstantMessageAddressesKey: String](nsmetadataiteminstantmessageaddresseskey.md)
- [let NSMetadataItemInstructionsKey: String](nsmetadataiteminstructionskey.md)
- [let NSMetadataItemIsApplicationManagedKey: String](nsmetadataitemisapplicationmanagedkey.md)
- [let NSMetadataItemIsGeneralMIDISequenceKey: String](nsmetadataitemisgeneralmidisequencekey.md)
- [let NSMetadataItemIsLikelyJunkKey: String](nsmetadataitemislikelyjunkkey.md)
- [let NSMetadataItemKeySignatureKey: String](nsmetadataitemkeysignaturekey.md)
- [let NSMetadataItemKeywordsKey: String](nsmetadataitemkeywordskey.md)
- [let NSMetadataItemKindKey: String](nsmetadataitemkindkey.md)
- [let NSMetadataItemLanguagesKey: String](nsmetadataitemlanguageskey.md)
- [let NSMetadataItemLastUsedDateKey: String](nsmetadataitemlastuseddatekey.md)
- [let NSMetadataItemLatitudeKey: String](nsmetadataitemlatitudekey.md)
- [let NSMetadataItemLayerNamesKey: String](nsmetadataitemlayernameskey.md)
- [let NSMetadataItemLensModelKey: String](nsmetadataitemlensmodelkey.md)
- [let NSMetadataItemLongitudeKey: String](nsmetadataitemlongitudekey.md)
- [let NSMetadataItemLyricistKey: String](nsmetadataitemlyricistkey.md)
- [let NSMetadataItemMaxApertureKey: String](nsmetadataitemmaxaperturekey.md)
- [let NSMetadataItemMediaTypesKey: String](nsmetadataitemmediatypeskey.md)
- [let NSMetadataItemMeteringModeKey: String](nsmetadataitemmeteringmodekey.md)
- [let NSMetadataItemMusicalGenreKey: String](nsmetadataitemmusicalgenrekey.md)
- [let NSMetadataItemMusicalInstrumentCategoryKey: String](nsmetadataitemmusicalinstrumentcategorykey.md)
- [let NSMetadataItemMusicalInstrumentNameKey: String](nsmetadataitemmusicalinstrumentnamekey.md)
- [let NSMetadataItemNamedLocationKey: String](nsmetadataitemnamedlocationkey.md)
- [let NSMetadataItemNumberOfPagesKey: String](nsmetadataitemnumberofpageskey.md)
- [let NSMetadataItemOrganizationsKey: String](nsmetadataitemorganizationskey.md)
- [let NSMetadataItemOrientationKey: String](nsmetadataitemorientationkey.md)
- [let NSMetadataItemOriginalFormatKey: String](nsmetadataitemoriginalformatkey.md)
- [let NSMetadataItemOriginalSourceKey: String](nsmetadataitemoriginalsourcekey.md)
- [let NSMetadataItemPageHeightKey: String](nsmetadataitempageheightkey.md)
- [let NSMetadataItemPageWidthKey: String](nsmetadataitempagewidthkey.md)
- [let NSMetadataItemParticipantsKey: String](nsmetadataitemparticipantskey.md)
- [let NSMetadataItemPerformersKey: String](nsmetadataitemperformerskey.md)
- [let NSMetadataItemPhoneNumbersKey: String](nsmetadataitemphonenumberskey.md)
- [let NSMetadataItemPixelCountKey: String](nsmetadataitempixelcountkey.md)
- [let NSMetadataItemPixelHeightKey: String](nsmetadataitempixelheightkey.md)
- [let NSMetadataItemPixelWidthKey: String](nsmetadataitempixelwidthkey.md)
- [let NSMetadataItemProducerKey: String](nsmetadataitemproducerkey.md)
- [let NSMetadataItemProfileNameKey: String](nsmetadataitemprofilenamekey.md)
- [let NSMetadataItemProjectsKey: String](nsmetadataitemprojectskey.md)
- [let NSMetadataItemPublishersKey: String](nsmetadataitempublisherskey.md)
- [let NSMetadataItemRecipientAddressesKey: String](nsmetadataitemrecipientaddresseskey.md)
- [let NSMetadataItemRecipientEmailAddressesKey: String](nsmetadataitemrecipientemailaddresseskey.md)
- [let NSMetadataItemRecipientsKey: String](nsmetadataitemrecipientskey.md)
- [let NSMetadataItemRecordingDateKey: String](nsmetadataitemrecordingdatekey.md)
- [let NSMetadataItemRecordingYearKey: String](nsmetadataitemrecordingyearkey.md)
- [let NSMetadataItemRedEyeOnOffKey: String](nsmetadataitemredeyeonoffkey.md)
- [let NSMetadataItemResolutionHeightDPIKey: String](nsmetadataitemresolutionheightdpikey.md)
- [let NSMetadataItemResolutionWidthDPIKey: String](nsmetadataitemresolutionwidthdpikey.md)
- [let NSMetadataItemRightsKey: String](nsmetadataitemrightskey.md)
- [let NSMetadataItemSecurityMethodKey: String](nsmetadataitemsecuritymethodkey.md)
- [let NSMetadataItemSpeedKey: String](nsmetadataitemspeedkey.md)
- [let NSMetadataItemStarRatingKey: String](nsmetadataitemstarratingkey.md)
- [let NSMetadataItemStateOrProvinceKey: String](nsmetadataitemstateorprovincekey.md)
- [let NSMetadataItemStreamableKey: String](nsmetadataitemstreamablekey.md)
- [let NSMetadataItemSubjectKey: String](nsmetadataitemsubjectkey.md)
- [let NSMetadataItemTempoKey: String](nsmetadataitemtempokey.md)
- [let NSMetadataItemTextContentKey: String](nsmetadataitemtextcontentkey.md)
- [let NSMetadataItemThemeKey: String](nsmetadataitemthemekey.md)
- [let NSMetadataItemTimeSignatureKey: String](nsmetadataitemtimesignaturekey.md)
- [let NSMetadataItemTimestampKey: String](nsmetadataitemtimestampkey.md)
- [let NSMetadataItemTitleKey: String](nsmetadataitemtitlekey.md)
- [let NSMetadataItemTotalBitRateKey: String](nsmetadataitemtotalbitratekey.md)
- [let NSMetadataItemVersionKey: String](nsmetadataitemversionkey.md)
- [let NSMetadataItemVideoBitRateKey: String](nsmetadataitemvideobitratekey.md)
- [let NSMetadataItemWhereFromsKey: String](nsmetadataitemwherefromskey.md)
- [let NSMetadataItemWhiteBalanceKey: String](nsmetadataitemwhitebalancekey.md)
### iCloud Keys
- [let NSMetadataItemIsUbiquitousKey: String](nsmetadataitemisubiquitouskey.md)
- [let NSMetadataUbiquitousItemContainerDisplayNameKey: String](nsmetadataubiquitousitemcontainerdisplaynamekey.md)
  The display name of the container that stores the ubiquitous item.
- [let NSMetadataUbiquitousItemDownloadRequestedKey: String](nsmetadataubiquitousitemdownloadrequestedkey.md)
  A Boolean value indicating whether a download has been requested for the ubiquitous item.
- [let NSMetadataUbiquitousItemIsExternalDocumentKey: String](nsmetadataubiquitousitemisexternaldocumentkey.md)
  A Boolean value indicating whether the ubiquitous item is from an external document.
- [let NSMetadataUbiquitousItemURLInLocalContainerKey: String](nsmetadataubiquitousitemurlinlocalcontainerkey.md)
  The URL for the ubiquitous item in the local container.
- [let NSMetadataUbiquitousItemHasUnresolvedConflictsKey: String](nsmetadataubiquitousitemhasunresolvedconflictskey.md)
- [let NSMetadataUbiquitousItemIsDownloadedKey: String](nsmetadataubiquitousitemisdownloadedkey.md)
- [let NSMetadataUbiquitousItemIsDownloadingKey: String](nsmetadataubiquitousitemisdownloadingkey.md)
- [let NSMetadataUbiquitousItemIsUploadedKey: String](nsmetadataubiquitousitemisuploadedkey.md)
- [let NSMetadataUbiquitousItemIsUploadingKey: String](nsmetadataubiquitousitemisuploadingkey.md)
- [let NSMetadataUbiquitousItemPercentDownloadedKey: String](nsmetadataubiquitousitempercentdownloadedkey.md)
- [let NSMetadataUbiquitousItemPercentUploadedKey: String](nsmetadataubiquitousitempercentuploadedkey.md)
- [let NSMetadataUbiquitousItemDownloadingStatusKey: String](nsmetadataubiquitousitemdownloadingstatuskey.md)
- [let NSMetadataUbiquitousItemDownloadingErrorKey: String](nsmetadataubiquitousitemdownloadingerrorkey.md)
- [let NSMetadataUbiquitousItemUploadingErrorKey: String](nsmetadataubiquitousitemuploadingerrorkey.md)
- [let NSMetadataUbiquitousItemIsSharedKey: String](nsmetadataubiquitousitemissharedkey.md)
  A Boolean value indicating whether the ubiquitous item is shared.
- [let NSMetadataUbiquitousSharedItemCurrentUserPermissionsKey: String](nsmetadataubiquitousshareditemcurrentuserpermissionskey.md)
  The permissions for the current user, or `nil` if not shared.
- [let NSMetadataUbiquitousSharedItemCurrentUserRoleKey: String](nsmetadataubiquitousshareditemcurrentuserrolekey.md)
  The current user’s role for the shared item, or `nil` if not shared.
- [let NSMetadataUbiquitousSharedItemMostRecentEditorNameComponentsKey: String](nsmetadataubiquitousshareditemmostrecenteditornamecomponentskey.md)
  The name components of the most recent editor of the shared document, or `nil` if it is the current user.
- [let NSMetadataUbiquitousSharedItemOwnerNameComponentsKey: String](nsmetadataubiquitousshareditemownernamecomponentskey.md)
  The name components of the shared item’s owner, or `nil` if the current user is the owner.
### iCloud Download Status Values
- [let NSMetadataUbiquitousItemDownloadingStatusCurrent: String](nsmetadataubiquitousitemdownloadingstatuscurrent.md)
- [let NSMetadataUbiquitousItemDownloadingStatusDownloaded: String](nsmetadataubiquitousitemdownloadingstatusdownloaded.md)
- [let NSMetadataUbiquitousItemDownloadingStatusNotDownloaded: String](nsmetadataubiquitousitemdownloadingstatusnotdownloaded.md)
### iCloud Sharing Permissions Values
- [let NSMetadataUbiquitousSharedItemPermissionsReadOnly: String](nsmetadataubiquitousshareditempermissionsreadonly.md)
  The current user is only allowed to read this item.
- [let NSMetadataUbiquitousSharedItemPermissionsReadWrite: String](nsmetadataubiquitousshareditempermissionsreadwrite.md)
  The current user is allowed to both read and write this item.
### iCloud Sharing Role Values
- [let NSMetadataUbiquitousSharedItemRoleOwner: String](nsmetadataubiquitousshareditemroleowner.md)
  The current user is the owner of the shared item.
- [let NSMetadataUbiquitousSharedItemRoleParticipant: String](nsmetadataubiquitousshareditemroleparticipant.md)
  The current user is a participant of the shared item.
### Initializers
- [init?(URL: URL)](nsmetadataitem/init(url:)-viww.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class NSMetadataQuery](nsmetadataquery.md)
  A query that you perform against Spotlight metadata.
- [protocol NSMetadataQueryDelegate](nsmetadataquerydelegate.md)
  An interface that enables the delegate of a metadata query to provide substitute results or attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataitem)*