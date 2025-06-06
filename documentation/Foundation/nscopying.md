# NSCopying

**Framework**: Foundation  
**Kind**: protocol

A protocol that objects adopt to provide functional copies of themselves.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol NSCopying
```

#### Overview

The exact meaning of “copy” can vary from class to class, but a copy must be a functionally independent object with values identical to the original at the time the copy was made. A copy produced with [`NSCopying`](nscopying.md) is implicitly retained by the sender, who is responsible for releasing it.

[`NSCopying`](nscopying.md) declares one method, [`copy(with:)`](nscopying/copy(with:).md), but copying is commonly invoked with the convenience method [`copy()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/copy()). The [`copy()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/copy()) method is defined for all objects inheriting from [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class) and simply invokes [`copy(with:)`](nscopying/copy(with:).md) with the default zone.

Your options for implementing this protocol are as follows:

- Implement [`NSCopying`](nscopying.md) using [`alloc`](https://developer.apple.com/documentation/objectivec/nsobject/1571958-alloc) and `init...` in classes that don’t inherit [`copy(with:)`](nscopying/copy(with:).md).
- Implement [`NSCopying`](nscopying.md) by invoking the superclass’s [`copy(with:)`](nscopying/copy(with:).md) when `NSCopying` behavior is inherited. If the superclass implementation might use the [`NSCopyObject`](nscopyobject.md) function, make explicit assignments to pointer instance variables for retained objects.
- Implement [`NSCopying`](nscopying.md) by retaining the original instead of creating a new copy when the class and its contents are immutable.

If a subclass inherits [`NSCopying`](nscopying.md) from its superclass and declares additional instance variables, the subclass has to override [`copy(with:)`](nscopying/copy(with:).md) to properly handle its own instance variables, invoking the superclass’s implementation first.

## Topics

### Copying
- [func copy(with: NSZone?) -> Any](nscopying/copy(with:).md)
  Returns a new instance that’s a copy of the receiver.

## Relationships

### Conforming Types
- [ByteCountFormatter](bytecountformatter.md)
- [CachedURLResponse](cachedurlresponse.md)
- [DateComponentsFormatter](datecomponentsformatter.md)
- [DateFormatter](dateformatter.md)
- [DateIntervalFormatter](dateintervalformatter.md)
- [Dimension](dimension.md)
- [EnergyFormatter](energyformatter.md)
- [Formatter](formatter.md)
- [HTTPURLResponse](httpurlresponse.md)
- [ISO8601DateFormatter](iso8601dateformatter.md)
- [LengthFormatter](lengthformatter.md)
- [ListFormatter](listformatter.md)
- [MassFormatter](massformatter.md)
- [MeasurementFormatter](measurementformatter.md)
- [MessagePort](messageport.md)
- [NSAffineTransform](nsaffinetransform.md)
- [NSAppleEventDescriptor](nsappleeventdescriptor.md)
- [NSAppleScript](nsapplescript.md)
- [NSArray](nsarray.md)
- [NSAttributedString](nsattributedstring.md)
- [NSCalendar](nscalendar.md)
- [NSCharacterSet](nscharacterset.md)
- [NSComparisonPredicate](nscomparisonpredicate.md)
- [NSCompoundPredicate](nscompoundpredicate.md)
- [NSCountedSet](nscountedset.md)
- [NSData](nsdata.md)
- [NSDataDetector](nsdatadetector.md)
- [NSDate](nsdate.md)
- [NSDateComponents](nsdatecomponents.md)
- [NSDateInterval](nsdateinterval.md)
- [NSDecimalNumber](nsdecimalnumber.md)
- [NSDictionary](nsdictionary.md)
- [NSError](nserror.md)
- [NSException](nsexception.md)
- [NSExpression](nsexpression.md)
- [NSExtensionItem](nsextensionitem.md)
- [NSFileSecurity](nsfilesecurity.md)
- [NSHashTable](nshashtable.md)
- [NSIndexPath](nsindexpath.md)
- [NSIndexSet](nsindexset.md)
- [NSItemProvider](nsitemprovider.md)
- [NSLocale](nslocale.md)
- [NSMachPort](nsmachport.md)
- [NSMapTable](nsmaptable.md)
- [NSMeasurement](nsmeasurement.md)
- [NSMutableArray](nsmutablearray.md)
- [NSMutableAttributedString](nsmutableattributedstring.md)
- [NSMutableCharacterSet](nsmutablecharacterset.md)
- [NSMutableData](nsmutabledata.md)
- [NSMutableDictionary](nsmutabledictionary.md)
- [NSMutableIndexSet](nsmutableindexset.md)
- [NSMutableOrderedSet](nsmutableorderedset.md)
- [NSMutableSet](nsmutableset.md)
- [NSMutableString](nsmutablestring.md)
- [NSMutableURLRequest](nsmutableurlrequest.md)
- [NSNotification](nsnotification.md)
- [NSNull](nsnull.md)
- [NSNumber](nsnumber.md)
- [NSOrderedSet](nsorderedset.md)
- [NSOrthography](nsorthography.md)
- [NSPersonNameComponents](nspersonnamecomponents.md)
- [NSPointerArray](nspointerarray.md)
- [NSPointerFunctions](nspointerfunctions.md)
- [NSPredicate](nspredicate.md)
- [NSPurgeableData](nspurgeabledata.md)
- [NSRegularExpression](nsregularexpression.md)
- [NSSet](nsset.md)
- [NSSortDescriptor](nssortdescriptor.md)
- [NSString](nsstring.md)
- [NSTextCheckingResult](nstextcheckingresult.md)
- [NSTimeZone](nstimezone.md)
- [NSURL](nsurl.md)
- [NSURLComponents](nsurlcomponents.md)
- [NSURLQueryItem](nsurlqueryitem.md)
- [NSURLRequest](nsurlrequest.md)
- [NSUUID](nsuuid.md)
- [NSUserNotification](nsusernotification.md)
- [NSUserNotificationAction](nsusernotificationaction.md)
- [NSValue](nsvalue.md)
- [NumberFormatter](numberformatter.md)
- [PersonNameComponentsFormatter](personnamecomponentsformatter.md)
- [Port](port.md)
- [RelativeDateTimeFormatter](relativedatetimeformatter.md)
- [Scanner](scanner.md)
- [SocketPort](socketport.md)
- [URLCredential](urlcredential.md)
- [URLProtectionSpace](urlprotectionspace.md)
- [URLResponse](urlresponse.md)
- [URLSessionConfiguration](urlsessionconfiguration.md)
- [URLSessionDataTask](urlsessiondatatask.md)
- [URLSessionDownloadTask](urlsessiondownloadtask.md)
- [URLSessionStreamTask](urlsessionstreamtask.md)
- [URLSessionTask](urlsessiontask.md)
- [URLSessionUploadTask](urlsessionuploadtask.md)
- [URLSessionWebSocketTask](urlsessionwebsockettask.md)
- [Unit](unit.md)
- [UnitAcceleration](unitacceleration.md)
- [UnitAngle](unitangle.md)
- [UnitArea](unitarea.md)
- [UnitConcentrationMass](unitconcentrationmass.md)
- [UnitDispersion](unitdispersion.md)
- [UnitDuration](unitduration.md)
- [UnitElectricCharge](unitelectriccharge.md)
- [UnitElectricCurrent](unitelectriccurrent.md)
- [UnitElectricPotentialDifference](unitelectricpotentialdifference.md)
- [UnitElectricResistance](unitelectricresistance.md)
- [UnitEnergy](unitenergy.md)
- [UnitFrequency](unitfrequency.md)
- [UnitFuelEfficiency](unitfuelefficiency.md)
- [UnitIlluminance](unitilluminance.md)
- [UnitInformationStorage](unitinformationstorage.md)
- [UnitLength](unitlength.md)
- [UnitMass](unitmass.md)
- [UnitPower](unitpower.md)
- [UnitPressure](unitpressure.md)
- [UnitSpeed](unitspeed.md)
- [UnitTemperature](unittemperature.md)
- [UnitVolume](unitvolume.md)
- [XMLDTD](xmldtd.md)
- [XMLDTDNode](xmldtdnode.md)
- [XMLDocument](xmldocument.md)
- [XMLElement](xmlelement.md)
- [XMLNode](xmlnode.md)

## See Also

- [protocol NSMutableCopying](nsmutablecopying.md)
  A protocol that mutable objects adopt to provide functional copies of themselves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscopying)*