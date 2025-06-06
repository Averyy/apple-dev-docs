# MTRClusterColorControl

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRClusterColorControl
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclustercolorcontrol/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustercolorcontrol/init(device:endpointid:queue:).md)
### Instance Methods
- [func colorLoopSet(with: MTRColorControlClusterColorLoopSetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/colorloopset(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func colorLoopSet(with: MTRColorControlClusterColorLoopSetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/colorloopset(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func enhancedMoveHue(with: MTRColorControlClusterEnhancedMoveHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/enhancedmovehue(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func enhancedMoveHue(with: MTRColorControlClusterEnhancedMoveHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/enhancedmovehue(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func enhancedMoveToHue(with: MTRColorControlClusterEnhancedMoveToHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/enhancedmovetohue(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func enhancedMoveToHue(with: MTRColorControlClusterEnhancedMoveToHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/enhancedmovetohue(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func enhancedMoveToHueAndSaturation(with: MTRColorControlClusterEnhancedMoveToHueAndSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/enhancedmovetohueandsaturation(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func enhancedMoveToHueAndSaturation(with: MTRColorControlClusterEnhancedMoveToHueAndSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/enhancedmovetohueandsaturation(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func enhancedStepHue(with: MTRColorControlClusterEnhancedStepHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/enhancedstephue(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func enhancedStepHue(with: MTRColorControlClusterEnhancedStepHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/enhancedstephue(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func moveColor(with: MTRColorControlClusterMoveColorParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/movecolor(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func moveColor(with: MTRColorControlClusterMoveColorParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/movecolor(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func moveColorTemperature(with: MTRColorControlClusterMoveColorTemperatureParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/movecolortemperature(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func moveColorTemperature(with: MTRColorControlClusterMoveColorTemperatureParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/movecolortemperature(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func moveHue(with: MTRColorControlClusterMoveHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/movehue(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func moveHue(with: MTRColorControlClusterMoveHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/movehue(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func moveSaturation(with: MTRColorControlClusterMoveSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/movesaturation(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func moveSaturation(with: MTRColorControlClusterMoveSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/movesaturation(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func moveToColor(with: MTRColorControlClusterMoveToColorParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/movetocolor(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func moveToColor(with: MTRColorControlClusterMoveToColorParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/movetocolor(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func moveToColorTemperature(with: MTRColorControlClusterMoveToColorTemperatureParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/movetocolortemperature(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func moveToColorTemperature(with: MTRColorControlClusterMoveToColorTemperatureParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/movetocolortemperature(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func moveToHue(with: MTRColorControlClusterMoveToHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/movetohue(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func moveToHue(with: MTRColorControlClusterMoveToHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/movetohue(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func moveToHueAndSaturation(with: MTRColorControlClusterMoveToHueAndSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/movetohueandsaturation(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func moveToHueAndSaturation(with: MTRColorControlClusterMoveToHueAndSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/movetohueandsaturation(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func moveToSaturation(with: MTRColorControlClusterMoveToSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/movetosaturation(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func moveToSaturation(with: MTRColorControlClusterMoveToSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/movetosaturation(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeclusterrevision(with:).md)
- [func readAttributeColorCapabilities(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorcapabilities(with:).md)
- [func readAttributeColorLoopActive(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorloopactive(with:).md)
- [func readAttributeColorLoopDirection(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorloopdirection(with:).md)
- [func readAttributeColorLoopStartEnhancedHue(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorloopstartenhancedhue(with:).md)
- [func readAttributeColorLoopStoredEnhancedHue(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorloopstoredenhancedhue(with:).md)
- [func readAttributeColorLoopTime(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorlooptime(with:).md)
- [func readAttributeColorMode(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolormode(with:).md)
- [func readAttributeColorPointBIntensity(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorpointbintensity(with:).md)
- [func readAttributeColorPointBX(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorpointbx(with:).md)
- [func readAttributeColorPointBY(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorpointby(with:).md)
- [func readAttributeColorPointGIntensity(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorpointgintensity(with:).md)
- [func readAttributeColorPointGX(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorpointgx(with:).md)
- [func readAttributeColorPointGY(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorpointgy(with:).md)
- [func readAttributeColorPointRIntensity(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorpointrintensity(with:).md)
- [func readAttributeColorPointRX(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorpointrx(with:).md)
- [func readAttributeColorPointRY(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolorpointry(with:).md)
- [func readAttributeColorTempPhysicalMaxMireds(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolortempphysicalmaxmireds(with:).md)
- [func readAttributeColorTempPhysicalMinMireds(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolortempphysicalminmireds(with:).md)
- [func readAttributeColorTemperatureMireds(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecolortemperaturemireds(with:).md)
- [func readAttributeCompensationText(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecompensationtext(with:).md)
- [func readAttributeCoupleColorTempToLevelMinMireds(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecouplecolortemptolevelminmireds(with:).md)
- [func readAttributeCurrentHue(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecurrenthue(with:).md)
- [func readAttributeCurrentSaturation(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecurrentsaturation(with:).md)
- [func readAttributeCurrentX(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecurrentx(with:).md)
- [func readAttributeCurrentY(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributecurrenty(with:).md)
- [func readAttributeDriftCompensation(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributedriftcompensation(with:).md)
- [func readAttributeEnhancedColorMode(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeenhancedcolormode(with:).md)
- [func readAttributeEnhancedCurrentHue(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeenhancedcurrenthue(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributegeneratedcommandlist(with:).md)
- [func readAttributeNumberOfPrimaries(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributenumberofprimaries(with:).md)
- [func readAttributeOptions(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeoptions(with:).md)
- [func readAttributePrimary1Intensity(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary1intensity(with:).md)
- [func readAttributePrimary1X(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary1x(with:).md)
- [func readAttributePrimary1Y(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary1y(with:).md)
- [func readAttributePrimary2Intensity(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary2intensity(with:).md)
- [func readAttributePrimary2X(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary2x(with:).md)
- [func readAttributePrimary2Y(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary2y(with:).md)
- [func readAttributePrimary3Intensity(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary3intensity(with:).md)
- [func readAttributePrimary3X(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary3x(with:).md)
- [func readAttributePrimary3Y(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary3y(with:).md)
- [func readAttributePrimary4Intensity(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary4intensity(with:).md)
- [func readAttributePrimary4X(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary4x(with:).md)
- [func readAttributePrimary4Y(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary4y(with:).md)
- [func readAttributePrimary5Intensity(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary5intensity(with:).md)
- [func readAttributePrimary5X(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary5x(with:).md)
- [func readAttributePrimary5Y(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary5y(with:).md)
- [func readAttributePrimary6Intensity(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary6intensity(with:).md)
- [func readAttributePrimary6X(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary6x(with:).md)
- [func readAttributePrimary6Y(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeprimary6y(with:).md)
- [func readAttributeRemainingTime(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributeremainingtime(with:).md)
- [func readAttributeStartUpColorTemperatureMireds(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributestartupcolortemperaturemireds(with:).md)
- [func readAttributeWhitePointX(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributewhitepointx(with:).md)
- [func readAttributeWhitePointY(with: MTRReadParams?) -> [String : Any]?](mtrclustercolorcontrol/readattributewhitepointy(with:).md)
- [func stepColor(with: MTRColorControlClusterStepColorParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/stepcolor(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stepColor(with: MTRColorControlClusterStepColorParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/stepcolor(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func stepColorTemperature(with: MTRColorControlClusterStepColorTemperatureParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/stepcolortemperature(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stepColorTemperature(with: MTRColorControlClusterStepColorTemperatureParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/stepcolortemperature(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func stepHue(with: MTRColorControlClusterStepHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/stephue(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stepHue(with: MTRColorControlClusterStepHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/stephue(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func stepSaturation(with: MTRColorControlClusterStepSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/stepsaturation(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stepSaturation(with: MTRColorControlClusterStepSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/stepsaturation(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func stopMoveStep(with: MTRColorControlClusterStopMoveStepParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercolorcontrol/stopmovestep(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stopMoveStep(with: MTRColorControlClusterStopMoveStepParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustercolorcontrol/stopmovestep(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func writeAttributeColorPointBIntensity(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercolorcontrol/writeattributecolorpointbintensity(withvalue:expectedvalueinterval:).md)
- [func writeAttributeColorPointBIntensity(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercolorcontrol/writeattributecolorpointbintensity(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeColorPointBX(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercolorcontrol/writeattributecolorpointbx(withvalue:expectedvalueinterval:).md)
- [func writeAttributeColorPointBX(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercolorcontrol/writeattributecolorpointbx(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeColorPointBY(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercolorcontrol/writeattributecolorpointby(withvalue:expectedvalueinterval:).md)
- [func writeAttributeColorPointBY(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercolorcontrol/writeattributecolorpointby(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeColorPointGIntensity(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercolorcontrol/writeattributecolorpointgintensity(withvalue:expectedvalueinterval:).md)
- [func writeAttributeColorPointGIntensity(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercolorcontrol/writeattributecolorpointgintensity(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeColorPointGX(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercolorcontrol/writeattributecolorpointgx(withvalue:expectedvalueinterval:).md)
- [func writeAttributeColorPointGX(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercolorcontrol/writeattributecolorpointgx(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeColorPointGY(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercolorcontrol/writeattributecolorpointgy(withvalue:expectedvalueinterval:).md)
- [func writeAttributeColorPointGY(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercolorcontrol/writeattributecolorpointgy(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeColorPointRIntensity(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercolorcontrol/writeattributecolorpointrintensity(withvalue:expectedvalueinterval:).md)
- [func writeAttributeColorPointRIntensity(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercolorcontrol/writeattributecolorpointrintensity(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeColorPointRX(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercolorcontrol/writeattributecolorpointrx(withvalue:expectedvalueinterval:).md)
- [func writeAttributeColorPointRX(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercolorcontrol/writeattributecolorpointrx(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeColorPointRY(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercolorcontrol/writeattributecolorpointry(withvalue:expectedvalueinterval:).md)
- [func writeAttributeColorPointRY(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercolorcontrol/writeattributecolorpointry(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeOptions(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercolorcontrol/writeattributeoptions(withvalue:expectedvalueinterval:).md)
- [func writeAttributeOptions(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercolorcontrol/writeattributeoptions(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeStartUpColorTemperatureMireds(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercolorcontrol/writeattributestartupcolortemperaturemireds(withvalue:expectedvalueinterval:).md)
- [func writeAttributeStartUpColorTemperatureMireds(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercolorcontrol/writeattributestartupcolortemperaturemireds(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeWhitePointX(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercolorcontrol/writeattributewhitepointx(withvalue:expectedvalueinterval:).md)
- [func writeAttributeWhitePointX(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercolorcontrol/writeattributewhitepointx(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeWhitePointY(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercolorcontrol/writeattributewhitepointy(withvalue:expectedvalueinterval:).md)
- [func writeAttributeWhitePointY(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercolorcontrol/writeattributewhitepointy(withvalue:expectedvalueinterval:params:).md)

## Relationships

### Inherits From
- [MTRGenericCluster](mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustercolorcontrol)*