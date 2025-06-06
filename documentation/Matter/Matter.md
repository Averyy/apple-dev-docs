# Matter

**Framework**: Matter  
**Kind**: module

Communicate with and control smart home devices from a variety of manufacturers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

#### Overview

The [`Matter`](https://developer.apple.comhttps://csa-iot.org/all-solutions/matter/) smart home connectivity standard enables interoperability between various smart home devices and ecosystems. Use  [`MatterSupport`](https://developer.apple.com/documentation/MatterSupport)  to bring accessories onto a local network, then commission and control those accessories using Matter.

![A diagram showing communication between Matter and non-Matter devices within a home. At the center is a Matter-enabled iOS device that connects to a Matter garage door controller on the left and a Matter light switch on the right. The Matter light switch connects to a Matter lamp controller. There are also non-Matter devices in the diagram: an outlet switch, a HomePod, and an Apple TV.](https://docs-assets.developer.apple.com/published/4b3deaf9106818123cf2758f2c2e4511/media-4199669%402x.png)

To access a Matter accessory on a network, you must commission it. Commissioning provides credentials to enable secure communication and performs initial accessory configuration. Once you commission an accessory, it exposes areas of functionality called clusters that you use to control it. For example, a light exposes the On/Off cluster to control whether it’s on or off. A dimmable light also exposes the Level Control cluster to control its brightness.

## Topics

### Matter device onboarding
- [Onboarding a Matter device](onboarding-a-matter-device.md)
  Prepare your app to discover and control a Matter device.
### Matter device interactions
- [Controller initialization](controller-initialization.md)
  Initialize the object that controls Matter accessories.
- [Accessory commissioning](accessory-commissioning.md)
  Commission a Matter accessory onto a network.
- [Accessory control](accessory-control.md)
  Communicate with commissioned Matter accessories.
- [Clusters](clusters.md)
  Interact with groups of related functionality that Matter accessories expose.
### Reference
- [Other symbols](other-symbols.md)
- [Matter Constants](matter-constants.md)
- [Matter Functions](matter-functions.md)
### Classes
- [class MTRAccessControlClusterAccessRestrictionEntryStruct](mtraccesscontrolclusteraccessrestrictionentrystruct.md)
- [class MTRAccessControlClusterAccessRestrictionStruct](mtraccesscontrolclusteraccessrestrictionstruct.md)
- [class MTRAccessControlClusterCommissioningAccessRestrictionEntryStruct](mtraccesscontrolclustercommissioningaccessrestrictionentrystruct.md)
- [class MTRAccessControlClusterFabricRestrictionReviewUpdateEvent](mtraccesscontrolclusterfabricrestrictionreviewupdateevent.md)
- [class MTRAccessControlClusterReviewFabricRestrictionsParams](mtraccesscontrolclusterreviewfabricrestrictionsparams.md)
- [class MTRAccessControlClusterReviewFabricRestrictionsResponseParams](mtraccesscontrolclusterreviewfabricrestrictionsresponseparams.md)
- [class MTRAccountLoginClusterLoggedOutEvent](mtraccountloginclusterloggedoutevent.md)
- [class MTRAttributeValueWaiter](mtrattributevaluewaiter.md)
- [class MTRBaseClusterCommissionerControl](mtrbaseclustercommissionercontrol.md)
  Cluster Commissioner Control
- [class MTRBaseClusterContentAppObserver](mtrbaseclustercontentappobserver.md)
  Cluster Content App Observer
- [class MTRBaseClusterDeviceEnergyManagement](mtrbaseclusterdeviceenergymanagement.md)
  Cluster Device Energy Management
- [class MTRBaseClusterDeviceEnergyManagementMode](mtrbaseclusterdeviceenergymanagementmode.md)
  Cluster Device Energy Management Mode
- [class MTRBaseClusterDishwasherAlarm](mtrbaseclusterdishwasheralarm.md)
  Cluster Dishwasher Alarm
- [class MTRBaseClusterDishwasherMode](mtrbaseclusterdishwashermode.md)
  Cluster Dishwasher Mode
- [class MTRBaseClusterEnergyEVSE](mtrbaseclusterenergyevse.md)
  Cluster Energy EVSE
- [class MTRBaseClusterEnergyEVSEMode](mtrbaseclusterenergyevsemode.md)
  Cluster Energy EVSE Mode
- [class MTRBaseClusterICDManagement](mtrbaseclustericdmanagement.md)
  Cluster ICD Management
- [class MTRBaseClusterLaundryDryerControls](mtrbaseclusterlaundrydryercontrols.md)
  Cluster Laundry Dryer Controls
- [class MTRBaseClusterLaundryWasherControls](mtrbaseclusterlaundrywashercontrols.md)
  Cluster Laundry Washer Controls
- [class MTRBaseClusterLaundryWasherMode](mtrbaseclusterlaundrywashermode.md)
  Cluster Laundry Washer Mode
- [class MTRBaseClusterMessages](mtrbaseclustermessages.md)
  Cluster Messages
- [class MTRBaseClusterMicrowaveOvenControl](mtrbaseclustermicrowaveovencontrol.md)
  Cluster Microwave Oven Control
- [class MTRBaseClusterMicrowaveOvenMode](mtrbaseclustermicrowaveovenmode.md)
  Cluster Microwave Oven Mode
- [class MTRBaseClusterOvenCavityOperationalState](mtrbaseclusterovencavityoperationalstate.md)
  Cluster Oven Cavity Operational State
- [class MTRBaseClusterOvenMode](mtrbaseclusterovenmode.md)
  Cluster Oven Mode
- [class MTRBaseClusterPowerTopology](mtrbaseclusterpowertopology.md)
  Cluster Power Topology
- [class MTRBaseClusterRefrigeratorAlarm](mtrbaseclusterrefrigeratoralarm.md)
  Cluster Refrigerator Alarm
- [class MTRBaseClusterRefrigeratorAndTemperatureControlledCabinetMode](mtrbaseclusterrefrigeratorandtemperaturecontrolledcabinetmode.md)
  Cluster Refrigerator And Temperature Controlled Cabinet Mode
- [class MTRBaseClusterServiceArea](mtrbaseclusterservicearea.md)
  Cluster Service Area
- [class MTRBaseClusterTemperatureControl](mtrbaseclustertemperaturecontrol.md)
  Cluster Temperature Control
- [class MTRBaseClusterThreadBorderRouterManagement](mtrbaseclusterthreadborderroutermanagement.md)
  Cluster Thread Border Router Management
- [class MTRBaseClusterThreadNetworkDirectory](mtrbaseclusterthreadnetworkdirectory.md)
  Cluster Thread Network Directory
- [class MTRBaseClusterTimeSynchronization](mtrbaseclustertimesynchronization.md)
  Cluster Time Synchronization
- [class MTRBaseClusterWaterHeaterManagement](mtrbaseclusterwaterheatermanagement.md)
  Cluster Water Heater Management
- [class MTRBaseClusterWaterHeaterMode](mtrbaseclusterwaterheatermode.md)
  Cluster Water Heater Mode
- [class MTRBaseClusterWiFiNetworkManagement](mtrbaseclusterwifinetworkmanagement.md)
  Cluster Wi-Fi Network Management
- [class MTRBridgedDeviceBasicInformationClusterActiveChangedEvent](mtrbridgeddevicebasicinformationclusteractivechangedevent.md)
- [class MTRBridgedDeviceBasicInformationClusterKeepActiveParams](mtrbridgeddevicebasicinformationclusterkeepactiveparams.md)
- [class MTRChannelClusterCancelRecordProgramParams](mtrchannelclustercancelrecordprogramparams.md)
- [class MTRChannelClusterChannelPagingStruct](mtrchannelclusterchannelpagingstruct.md)
- [class MTRChannelClusterGetProgramGuideParams](mtrchannelclustergetprogramguideparams.md)
- [class MTRChannelClusterPageTokenStruct](mtrchannelclusterpagetokenstruct.md)
- [class MTRChannelClusterProgramCastStruct](mtrchannelclusterprogramcaststruct.md)
- [class MTRChannelClusterProgramCategoryStruct](mtrchannelclusterprogramcategorystruct.md)
- [class MTRChannelClusterProgramGuideResponseParams](mtrchannelclusterprogramguideresponseparams.md)
- [class MTRChannelClusterProgramStruct](mtrchannelclusterprogramstruct.md)
- [class MTRChannelClusterRecordProgramParams](mtrchannelclusterrecordprogramparams.md)
- [class MTRChannelClusterSeriesInfoStruct](mtrchannelclusterseriesinfostruct.md)
- [class MTRClusterCommissionerControl](mtrclustercommissionercontrol.md)
  Cluster Commissioner Control Supports the ability for clients to request the commissioning of themselves or other nodes onto a fabric which the cluster server can commission onto.
- [class MTRClusterContentAppObserver](mtrclustercontentappobserver.md)
  Cluster Content App Observer This cluster provides an interface for sending targeted commands to an Observer of a Content App on a Video Player device such as a Streaming Media Player, Smart TV or Smart Screen. The cluster server for Content App Observer is implemented by an endpoint that communicates with a Content App, such as a Casting Video Client. The cluster client for Content App Observer is implemented by a Content App endpoint. A Content App is informed of the NodeId of an Observer when a binding is set on the Content App. The Content App can then send the ContentAppMessage to the Observer (server cluster), and the Observer responds with a ContentAppMessageResponse.
- [class MTRClusterDeviceEnergyManagement](mtrclusterdeviceenergymanagement.md)
  Cluster Device Energy Management This cluster allows a client to manage the power draw of a device. An example of such a client could be an Energy Management System (EMS) which controls an Energy Smart Appliance (ESA).
- [class MTRClusterDeviceEnergyManagementMode](mtrclusterdeviceenergymanagementmode.md)
  Cluster Device Energy Management Mode Attributes and commands for selecting a mode from a list of supported options.
- [class MTRClusterDishwasherAlarm](mtrclusterdishwasheralarm.md)
  Cluster Dishwasher Alarm Attributes and commands for configuring the Dishwasher alarm.
- [class MTRClusterDishwasherMode](mtrclusterdishwashermode.md)
  Cluster Dishwasher Mode Attributes and commands for selecting a mode from a list of supported options.
- [class MTRClusterEnergyEVSE](mtrclusterenergyevse.md)
  Cluster Energy EVSE Electric Vehicle Supply Equipment (EVSE) is equipment used to charge an Electric Vehicle (EV) or Plug-In Hybrid Electric Vehicle. This cluster provides an interface to the functionality of Electric Vehicle Supply Equipment (EVSE) management.
- [class MTRClusterEnergyEVSEMode](mtrclusterenergyevsemode.md)
  Cluster Energy EVSE Mode Attributes and commands for selecting a mode from a list of supported options.
- [class MTRClusterICDManagement](mtrclustericdmanagement.md)
  Cluster ICD Management Allows servers to ensure that listed clients are notified when a server is available for communication.
- [class MTRClusterLaundryDryerControls](mtrclusterlaundrydryercontrols.md)
  Cluster Laundry Dryer Controls This cluster provides a way to access options associated with the operation of a laundry dryer device type.
- [class MTRClusterLaundryWasherControls](mtrclusterlaundrywashercontrols.md)
  Cluster Laundry Washer Controls This cluster supports remotely monitoring and controlling the different types of functionality available to a washing device, such as a washing machine.
- [class MTRClusterLaundryWasherMode](mtrclusterlaundrywashermode.md)
  Cluster Laundry Washer Mode Attributes and commands for selecting a mode from a list of supported options.
- [class MTRClusterMessages](mtrclustermessages.md)
  Cluster Messages This cluster provides an interface for passing messages to be presented by a device.
- [class MTRClusterMicrowaveOvenControl](mtrclustermicrowaveovencontrol.md)
  Cluster Microwave Oven Control Attributes and commands for configuring the microwave oven control, and reporting cooking stats.
- [class MTRClusterMicrowaveOvenMode](mtrclustermicrowaveovenmode.md)
  Cluster Microwave Oven Mode Attributes and commands for selecting a mode from a list of supported options.
- [class MTRClusterOvenCavityOperationalState](mtrclusterovencavityoperationalstate.md)
  Cluster Oven Cavity Operational State This cluster supports remotely monitoring and, where supported, changing the operational state of an Oven.
- [class MTRClusterOvenMode](mtrclusterovenmode.md)
  Cluster Oven Mode Attributes and commands for selecting a mode from a list of supported options.
- [class MTRClusterPowerTopology](mtrclusterpowertopology.md)
  Cluster Power Topology The Power Topology Cluster provides a mechanism for expressing how power is flowing between endpoints.
- [class MTRClusterRefrigeratorAlarm](mtrclusterrefrigeratoralarm.md)
  Cluster Refrigerator Alarm Attributes and commands for configuring the Refrigerator alarm.
- [class MTRClusterRefrigeratorAndTemperatureControlledCabinetMode](mtrclusterrefrigeratorandtemperaturecontrolledcabinetmode.md)
  Cluster Refrigerator And Temperature Controlled Cabinet Mode Attributes and commands for selecting a mode from a list of supported options.
- [class MTRClusterServiceArea](mtrclusterservicearea.md)
  Cluster Service Area The Service Area cluster provides an interface for controlling the areas where a device should operate, and for querying the current area being serviced.
- [class MTRClusterTemperatureControl](mtrclustertemperaturecontrol.md)
  Cluster Temperature Control Attributes and commands for configuring the temperature control, and reporting temperature.
- [class MTRClusterThreadBorderRouterManagement](mtrclusterthreadborderroutermanagement.md)
  Cluster Thread Border Router Management Manage the Thread network of Thread Border Router
- [class MTRClusterThreadNetworkDirectory](mtrclusterthreadnetworkdirectory.md)
  Cluster Thread Network Directory Manages the names and credentials of Thread networks visible to the user.
- [class MTRClusterTimeSynchronization](mtrclustertimesynchronization.md)
  Cluster Time Synchronization Accurate time is required for a number of reasons, including scheduling, display and validating security materials.
- [class MTRClusterWaterHeaterManagement](mtrclusterwaterheatermanagement.md)
  Cluster Water Heater Management This cluster is used to allow clients to control the operation of a hot water heating appliance so that it can be used with energy management.
- [class MTRClusterWaterHeaterMode](mtrclusterwaterheatermode.md)
  Cluster Water Heater Mode Attributes and commands for selecting a mode from a list of supported options.
- [class MTRClusterWiFiNetworkManagement](mtrclusterwifinetworkmanagement.md)
  Cluster Wi-Fi Network Management Functionality to retrieve operational information about a managed Wi-Fi network.
- [class MTRCommandWithRequiredResponse](mtrcommandwithrequiredresponse.md)
  An object representing a single command to be invoked and the response required for the invoke to be considered successful.
- [class MTRCommissioneeInfo](mtrcommissioneeinfo.md)
  Information read from the commissionee device during commissioning.
- [class MTRCommissionerControlClusterCommissionNodeParams](mtrcommissionercontrolclustercommissionnodeparams.md)
- [class MTRCommissionerControlClusterCommissioningRequestResultEvent](mtrcommissionercontrolclustercommissioningrequestresultevent.md)
- [class MTRCommissionerControlClusterRequestCommissioningApprovalParams](mtrcommissionercontrolclusterrequestcommissioningapprovalparams.md)
- [class MTRCommissionerControlClusterReverseOpenCommissioningWindowParams](mtrcommissionercontrolclusterreverseopencommissioningwindowparams.md)
- [class MTRContentAppObserverClusterContentAppMessageParams](mtrcontentappobserverclustercontentappmessageparams.md)
- [class MTRContentAppObserverClusterContentAppMessageResponseParams](mtrcontentappobserverclustercontentappmessageresponseparams.md)
- [class MTRDataTypeAtomicAttributeStatusStruct](mtrdatatypeatomicattributestatusstruct.md)
- [class MTRDataTypeLocationDescriptorStruct](mtrdatatypelocationdescriptorstruct.md)
- [class MTRDeviceEnergyManagementClusterCancelPowerAdjustRequestParams](mtrdeviceenergymanagementclustercancelpoweradjustrequestparams.md)
- [class MTRDeviceEnergyManagementClusterCancelRequestParams](mtrdeviceenergymanagementclustercancelrequestparams.md)
- [class MTRDeviceEnergyManagementClusterConstraintsStruct](mtrdeviceenergymanagementclusterconstraintsstruct.md)
- [class MTRDeviceEnergyManagementClusterCostStruct](mtrdeviceenergymanagementclustercoststruct.md)
- [class MTRDeviceEnergyManagementClusterForecastStruct](mtrdeviceenergymanagementclusterforecaststruct.md)
- [class MTRDeviceEnergyManagementClusterModifyForecastRequestParams](mtrdeviceenergymanagementclustermodifyforecastrequestparams.md)
- [class MTRDeviceEnergyManagementClusterPauseRequestParams](mtrdeviceenergymanagementclusterpauserequestparams.md)
- [class MTRDeviceEnergyManagementClusterPausedEvent](mtrdeviceenergymanagementclusterpausedevent.md)
- [class MTRDeviceEnergyManagementClusterPowerAdjustCapabilityStruct](mtrdeviceenergymanagementclusterpoweradjustcapabilitystruct.md)
- [class MTRDeviceEnergyManagementClusterPowerAdjustEndEvent](mtrdeviceenergymanagementclusterpoweradjustendevent.md)
- [class MTRDeviceEnergyManagementClusterPowerAdjustRequestParams](mtrdeviceenergymanagementclusterpoweradjustrequestparams.md)
- [class MTRDeviceEnergyManagementClusterPowerAdjustStartEvent](mtrdeviceenergymanagementclusterpoweradjuststartevent.md)
- [class MTRDeviceEnergyManagementClusterPowerAdjustStruct](mtrdeviceenergymanagementclusterpoweradjuststruct.md)
- [class MTRDeviceEnergyManagementClusterRequestConstraintBasedForecastParams](mtrdeviceenergymanagementclusterrequestconstraintbasedforecastparams.md)
- [class MTRDeviceEnergyManagementClusterResumeRequestParams](mtrdeviceenergymanagementclusterresumerequestparams.md)
- [class MTRDeviceEnergyManagementClusterResumedEvent](mtrdeviceenergymanagementclusterresumedevent.md)
- [class MTRDeviceEnergyManagementClusterSlotAdjustmentStruct](mtrdeviceenergymanagementclusterslotadjustmentstruct.md)
- [class MTRDeviceEnergyManagementClusterSlotStruct](mtrdeviceenergymanagementclusterslotstruct.md)
- [class MTRDeviceEnergyManagementClusterStartTimeAdjustRequestParams](mtrdeviceenergymanagementclusterstarttimeadjustrequestparams.md)
- [class MTRDeviceEnergyManagementModeClusterChangeToModeParams](mtrdeviceenergymanagementmodeclusterchangetomodeparams.md)
- [class MTRDeviceEnergyManagementModeClusterChangeToModeResponseParams](mtrdeviceenergymanagementmodeclusterchangetomoderesponseparams.md)
- [class MTRDeviceEnergyManagementModeClusterModeOptionStruct](mtrdeviceenergymanagementmodeclustermodeoptionstruct.md)
- [class MTRDeviceEnergyManagementModeClusterModeTagStruct](mtrdeviceenergymanagementmodeclustermodetagstruct.md)
- [class MTRDeviceType](mtrdevicetype.md)
  Meta-data about a device type defined in the Matter specification.
- [class MTRDishwasherAlarmClusterModifyEnabledAlarmsParams](mtrdishwasheralarmclustermodifyenabledalarmsparams.md)
- [class MTRDishwasherAlarmClusterNotifyEvent](mtrdishwasheralarmclusternotifyevent.md)
- [class MTRDishwasherAlarmClusterResetParams](mtrdishwasheralarmclusterresetparams.md)
- [class MTRDishwasherModeClusterChangeToModeParams](mtrdishwashermodeclusterchangetomodeparams.md)
- [class MTRDishwasherModeClusterChangeToModeResponseParams](mtrdishwashermodeclusterchangetomoderesponseparams.md)
- [class MTRDishwasherModeClusterModeOptionStruct](mtrdishwashermodeclustermodeoptionstruct.md)
- [class MTRDishwasherModeClusterModeTagStruct](mtrdishwashermodeclustermodetagstruct.md)
- [class MTRDoorLockClusterClearAliroReaderConfigParams](mtrdoorlockclusterclearaliroreaderconfigparams.md)
- [class MTRDoorLockClusterSetAliroReaderConfigParams](mtrdoorlockclustersetaliroreaderconfigparams.md)
- [class MTRDoorLockClusterUnboltDoorParams](mtrdoorlockclusterunboltdoorparams.md)
- [class MTRElectricalEnergyMeasurementClusterMeasurementAccuracyRangeStruct](mtrelectricalenergymeasurementclustermeasurementaccuracyrangestruct.md)
- [class MTREndpointInfo](mtrendpointinfo.md)
  Meta-data about an endpoint of a Matter node.
- [class MTREnergyEVSEClusterChargingTargetScheduleStruct](mtrenergyevseclusterchargingtargetschedulestruct.md)
- [class MTREnergyEVSEClusterChargingTargetStruct](mtrenergyevseclusterchargingtargetstruct.md)
- [class MTREnergyEVSEClusterClearTargetsParams](mtrenergyevseclustercleartargetsparams.md)
- [class MTREnergyEVSEClusterDisableParams](mtrenergyevseclusterdisableparams.md)
- [class MTREnergyEVSEClusterEVConnectedEvent](mtrenergyevseclusterevconnectedevent.md)
- [class MTREnergyEVSEClusterEVNotDetectedEvent](mtrenergyevseclusterevnotdetectedevent.md)
- [class MTREnergyEVSEClusterEnableChargingParams](mtrenergyevseclusterenablechargingparams.md)
- [class MTREnergyEVSEClusterEnergyTransferStartedEvent](mtrenergyevseclusterenergytransferstartedevent.md)
- [class MTREnergyEVSEClusterEnergyTransferStoppedEvent](mtrenergyevseclusterenergytransferstoppedevent.md)
- [class MTREnergyEVSEClusterFaultEvent](mtrenergyevseclusterfaultevent.md)
- [class MTREnergyEVSEClusterGetTargetsParams](mtrenergyevseclustergettargetsparams.md)
- [class MTREnergyEVSEClusterGetTargetsResponseParams](mtrenergyevseclustergettargetsresponseparams.md)
- [class MTREnergyEVSEClusterRFIDEvent](mtrenergyevseclusterrfidevent.md)
- [class MTREnergyEVSEClusterSetTargetsParams](mtrenergyevseclustersettargetsparams.md)
- [class MTREnergyEVSEClusterStartDiagnosticsParams](mtrenergyevseclusterstartdiagnosticsparams.md)
- [class MTREnergyEVSEModeClusterChangeToModeParams](mtrenergyevsemodeclusterchangetomodeparams.md)
- [class MTREnergyEVSEModeClusterChangeToModeResponseParams](mtrenergyevsemodeclusterchangetomoderesponseparams.md)
- [class MTREnergyEVSEModeClusterModeOptionStruct](mtrenergyevsemodeclustermodeoptionstruct.md)
- [class MTREnergyEVSEModeClusterModeTagStruct](mtrenergyevsemodeclustermodetagstruct.md)
- [class MTRGeneralDiagnosticsClusterPayloadTestRequestParams](mtrgeneraldiagnosticsclusterpayloadtestrequestparams.md)
- [class MTRGeneralDiagnosticsClusterPayloadTestResponseParams](mtrgeneraldiagnosticsclusterpayloadtestresponseparams.md)
- [class MTRGeneralDiagnosticsClusterTimeSnapshotParams](mtrgeneraldiagnosticsclustertimesnapshotparams.md)
- [class MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams](mtrgeneraldiagnosticsclustertimesnapshotresponseparams.md)
- [class MTRICDManagementClusterMonitoringRegistrationStruct](mtricdmanagementclustermonitoringregistrationstruct.md)
- [class MTRICDManagementClusterRegisterClientParams](mtricdmanagementclusterregisterclientparams.md)
- [class MTRICDManagementClusterRegisterClientResponseParams](mtricdmanagementclusterregisterclientresponseparams.md)
- [class MTRICDManagementClusterStayActiveRequestParams](mtricdmanagementclusterstayactiverequestparams.md)
- [class MTRICDManagementClusterStayActiveResponseParams](mtricdmanagementclusterstayactiveresponseparams.md)
- [class MTRICDManagementClusterUnregisterClientParams](mtricdmanagementclusterunregisterclientparams.md)
- [class MTRLaundryWasherModeClusterChangeToModeParams](mtrlaundrywashermodeclusterchangetomodeparams.md)
- [class MTRLaundryWasherModeClusterChangeToModeResponseParams](mtrlaundrywashermodeclusterchangetomoderesponseparams.md)
- [class MTRLaundryWasherModeClusterModeOptionStruct](mtrlaundrywashermodeclustermodeoptionstruct.md)
- [class MTRLaundryWasherModeClusterModeTagStruct](mtrlaundrywashermodeclustermodetagstruct.md)
- [class MTRMediaPlaybackClusterActivateAudioTrackParams](mtrmediaplaybackclusteractivateaudiotrackparams.md)
- [class MTRMediaPlaybackClusterActivateTextTrackParams](mtrmediaplaybackclusteractivatetexttrackparams.md)
- [class MTRMediaPlaybackClusterDeactivateTextTrackParams](mtrmediaplaybackclusterdeactivatetexttrackparams.md)
- [class MTRMediaPlaybackClusterStateChangedEvent](mtrmediaplaybackclusterstatechangedevent.md)
- [class MTRMessagesClusterCancelMessagesRequestParams](mtrmessagesclustercancelmessagesrequestparams.md)
- [class MTRMessagesClusterMessageCompleteEvent](mtrmessagesclustermessagecompleteevent.md)
- [class MTRMessagesClusterMessagePresentedEvent](mtrmessagesclustermessagepresentedevent.md)
- [class MTRMessagesClusterMessageQueuedEvent](mtrmessagesclustermessagequeuedevent.md)
- [class MTRMessagesClusterMessageResponseOptionStruct](mtrmessagesclustermessageresponseoptionstruct.md)
- [class MTRMessagesClusterMessageStruct](mtrmessagesclustermessagestruct.md)
- [class MTRMessagesClusterPresentMessagesRequestParams](mtrmessagesclusterpresentmessagesrequestparams.md)
- [class MTRMicrowaveOvenControlClusterAddMoreTimeParams](mtrmicrowaveovencontrolclusteraddmoretimeparams.md)
- [class MTRMicrowaveOvenControlClusterSetCookingParametersParams](mtrmicrowaveovencontrolclustersetcookingparametersparams.md)
- [class MTRMicrowaveOvenModeClusterModeOptionStruct](mtrmicrowaveovenmodeclustermodeoptionstruct.md)
- [class MTRMicrowaveOvenModeClusterModeTagStruct](mtrmicrowaveovenmodeclustermodetagstruct.md)
- [class MTROccupancySensingClusterHoldTimeLimitsStruct](mtroccupancysensingclusterholdtimelimitsstruct.md)
- [class MTROccupancySensingClusterOccupancyChangedEvent](mtroccupancysensingclusteroccupancychangedevent.md)
- [class MTROvenCavityOperationalStateClusterErrorStateStruct](mtrovencavityoperationalstateclustererrorstatestruct.md)
- [class MTROvenCavityOperationalStateClusterOperationCompletionEvent](mtrovencavityoperationalstateclusteroperationcompletionevent.md)
- [class MTROvenCavityOperationalStateClusterOperationalCommandResponseParams](mtrovencavityoperationalstateclusteroperationalcommandresponseparams.md)
- [class MTROvenCavityOperationalStateClusterOperationalErrorEvent](mtrovencavityoperationalstateclusteroperationalerrorevent.md)
- [class MTROvenCavityOperationalStateClusterOperationalStateStruct](mtrovencavityoperationalstateclusteroperationalstatestruct.md)
- [class MTROvenCavityOperationalStateClusterStartParams](mtrovencavityoperationalstateclusterstartparams.md)
- [class MTROvenCavityOperationalStateClusterStopParams](mtrovencavityoperationalstateclusterstopparams.md)
- [class MTROvenModeClusterChangeToModeParams](mtrovenmodeclusterchangetomodeparams.md)
- [class MTROvenModeClusterChangeToModeResponseParams](mtrovenmodeclusterchangetomoderesponseparams.md)
- [class MTROvenModeClusterModeOptionStruct](mtrovenmodeclustermodeoptionstruct.md)
- [class MTROvenModeClusterModeTagStruct](mtrovenmodeclustermodetagstruct.md)
- [class MTRRVCOperationalStateClusterGoHomeParams](mtrrvcoperationalstateclustergohomeparams.md)
- [class MTRRefrigeratorAlarmClusterNotifyEvent](mtrrefrigeratoralarmclusternotifyevent.md)
- [class MTRRefrigeratorAndTemperatureControlledCabinetModeClusterChangeToModeParams](mtrrefrigeratorandtemperaturecontrolledcabinetmodeclusterchangetomodeparams.md)
- [class MTRRefrigeratorAndTemperatureControlledCabinetModeClusterChangeToModeResponseParams](mtrrefrigeratorandtemperaturecontrolledcabinetmodeclusterchangetomoderesponseparams.md)
- [class MTRRefrigeratorAndTemperatureControlledCabinetModeClusterModeOptionStruct](mtrrefrigeratorandtemperaturecontrolledcabinetmodeclustermodeoptionstruct.md)
- [class MTRRefrigeratorAndTemperatureControlledCabinetModeClusterModeTagStruct](mtrrefrigeratorandtemperaturecontrolledcabinetmodeclustermodetagstruct.md)
- [class MTRServiceAreaClusterAreaInfoStruct](mtrserviceareaclusterareainfostruct.md)
- [class MTRServiceAreaClusterAreaStruct](mtrserviceareaclusterareastruct.md)
- [class MTRServiceAreaClusterLandmarkInfoStruct](mtrserviceareaclusterlandmarkinfostruct.md)
- [class MTRServiceAreaClusterMapStruct](mtrserviceareaclustermapstruct.md)
- [class MTRServiceAreaClusterProgressStruct](mtrserviceareaclusterprogressstruct.md)
- [class MTRServiceAreaClusterSelectAreasParams](mtrserviceareaclusterselectareasparams.md)
- [class MTRServiceAreaClusterSelectAreasResponseParams](mtrserviceareaclusterselectareasresponseparams.md)
- [class MTRServiceAreaClusterSkipAreaParams](mtrserviceareaclusterskipareaparams.md)
- [class MTRServiceAreaClusterSkipAreaResponseParams](mtrserviceareaclusterskiparearesponseparams.md)
- [class MTRTargetNavigatorClusterTargetUpdatedEvent](mtrtargetnavigatorclustertargetupdatedevent.md)
- [class MTRTemperatureControlClusterSetTemperatureParams](mtrtemperaturecontrolclustersettemperatureparams.md)
- [class MTRThermostatClusterAtomicRequestParams](mtrthermostatclusteratomicrequestparams.md)
- [class MTRThermostatClusterAtomicResponseParams](mtrthermostatclusteratomicresponseparams.md)
- [class MTRThermostatClusterPresetStruct](mtrthermostatclusterpresetstruct.md)
- [class MTRThermostatClusterPresetTypeStruct](mtrthermostatclusterpresettypestruct.md)
- [class MTRThermostatClusterScheduleStruct](mtrthermostatclusterschedulestruct.md)
- [class MTRThermostatClusterScheduleTransitionStruct](mtrthermostatclusterscheduletransitionstruct.md)
- [class MTRThermostatClusterScheduleTypeStruct](mtrthermostatclusterscheduletypestruct.md)
- [class MTRThermostatClusterSetActivePresetRequestParams](mtrthermostatclustersetactivepresetrequestparams.md)
- [class MTRThermostatClusterSetActiveScheduleRequestParams](mtrthermostatclustersetactiveschedulerequestparams.md)
- [class MTRThreadBorderRouterManagementClusterDatasetResponseParams](mtrthreadborderroutermanagementclusterdatasetresponseparams.md)
- [class MTRThreadBorderRouterManagementClusterGetActiveDatasetRequestParams](mtrthreadborderroutermanagementclustergetactivedatasetrequestparams.md)
- [class MTRThreadBorderRouterManagementClusterGetPendingDatasetRequestParams](mtrthreadborderroutermanagementclustergetpendingdatasetrequestparams.md)
- [class MTRThreadBorderRouterManagementClusterSetActiveDatasetRequestParams](mtrthreadborderroutermanagementclustersetactivedatasetrequestparams.md)
- [class MTRThreadBorderRouterManagementClusterSetPendingDatasetRequestParams](mtrthreadborderroutermanagementclustersetpendingdatasetrequestparams.md)
- [class MTRThreadNetworkDirectoryClusterAddNetworkParams](mtrthreadnetworkdirectoryclusteraddnetworkparams.md)
- [class MTRThreadNetworkDirectoryClusterGetOperationalDatasetParams](mtrthreadnetworkdirectoryclustergetoperationaldatasetparams.md)
- [class MTRThreadNetworkDirectoryClusterOperationalDatasetResponseParams](mtrthreadnetworkdirectoryclusteroperationaldatasetresponseparams.md)
- [class MTRThreadNetworkDirectoryClusterRemoveNetworkParams](mtrthreadnetworkdirectoryclusterremovenetworkparams.md)
- [class MTRThreadNetworkDirectoryClusterThreadNetworkStruct](mtrthreadnetworkdirectoryclusterthreadnetworkstruct.md)
- [class MTRTimeSynchronizationClusterDSTStatusEvent](mtrtimesynchronizationclusterdststatusevent.md)
- [class MTRTimeSynchronizationClusterDSTTableEmptyEvent](mtrtimesynchronizationclusterdsttableemptyevent.md)
- [class MTRTimeSynchronizationClusterFabricScopedTrustedTimeSourceStruct](mtrtimesynchronizationclusterfabricscopedtrustedtimesourcestruct.md)
- [class MTRTimeSynchronizationClusterMissingTrustedTimeSourceEvent](mtrtimesynchronizationclustermissingtrustedtimesourceevent.md)
- [class MTRTimeSynchronizationClusterSetDSTOffsetParams](mtrtimesynchronizationclustersetdstoffsetparams.md)
- [class MTRTimeSynchronizationClusterSetDefaultNTPParams](mtrtimesynchronizationclustersetdefaultntpparams.md)
- [class MTRTimeSynchronizationClusterSetTimeZoneParams](mtrtimesynchronizationclustersettimezoneparams.md)
- [class MTRTimeSynchronizationClusterSetTimeZoneResponseParams](mtrtimesynchronizationclustersettimezoneresponseparams.md)
- [class MTRTimeSynchronizationClusterSetTrustedTimeSourceParams](mtrtimesynchronizationclustersettrustedtimesourceparams.md)
- [class MTRTimeSynchronizationClusterTimeFailureEvent](mtrtimesynchronizationclustertimefailureevent.md)
- [class MTRTimeSynchronizationClusterTimeZoneStatusEvent](mtrtimesynchronizationclustertimezonestatusevent.md)
- [class MTRTimeSynchronizationClusterTrustedTimeSourceStruct](mtrtimesynchronizationclustertrustedtimesourcestruct.md)
- [class MTRWaterHeaterManagementClusterBoostEndedEvent](mtrwaterheatermanagementclusterboostendedevent.md)
- [class MTRWaterHeaterManagementClusterBoostParams](mtrwaterheatermanagementclusterboostparams.md)
- [class MTRWaterHeaterManagementClusterBoostStartedEvent](mtrwaterheatermanagementclusterbooststartedevent.md)
- [class MTRWaterHeaterManagementClusterCancelBoostParams](mtrwaterheatermanagementclustercancelboostparams.md)
- [class MTRWaterHeaterManagementClusterWaterHeaterBoostInfoStruct](mtrwaterheatermanagementclusterwaterheaterboostinfostruct.md)
- [class MTRWaterHeaterModeClusterChangeToModeParams](mtrwaterheatermodeclusterchangetomodeparams.md)
- [class MTRWaterHeaterModeClusterChangeToModeResponseParams](mtrwaterheatermodeclusterchangetomoderesponseparams.md)
- [class MTRWaterHeaterModeClusterModeOptionStruct](mtrwaterheatermodeclustermodeoptionstruct.md)
- [class MTRWaterHeaterModeClusterModeTagStruct](mtrwaterheatermodeclustermodetagstruct.md)
- [class MTRWiFiNetworkManagementClusterNetworkPassphraseRequestParams](mtrwifinetworkmanagementclusternetworkpassphraserequestparams.md)
- [class MTRWiFiNetworkManagementClusterNetworkPassphraseResponseParams](mtrwifinetworkmanagementclusternetworkpassphraseresponseparams.md)
- [class MTRXPCDeviceControllerParameters](mtrxpcdevicecontrollerparameters.md)
### Protocols
- [protocol MTRXPCClientProtocol](mtrxpcclientprotocol.md)
- [protocol MTRXPCClientProtocol_MTRDevice](mtrxpcclientprotocol_mtrdevice.md)
- [protocol MTRXPCClientProtocol_MTRDeviceController](mtrxpcclientprotocol_mtrdevicecontroller.md)
- [protocol MTRXPCServerProtocol](mtrxpcserverprotocol.md)
- [protocol MTRXPCServerProtocol_MTRDevice](mtrxpcserverprotocol_mtrdevice.md)
- [protocol MTRXPCServerProtocol_MTRDeviceController](mtrxpcserverprotocol_mtrdevicecontroller.md)
### Structures
- [struct MTRAccessControlFeature](mtraccesscontrolfeature.md)
- [struct MTRBridgedDeviceBasicInformationFeature](mtrbridgeddevicebasicinformationfeature.md)
- [struct MTRChannelRecordingFlagBitmap](mtrchannelrecordingflagbitmap.md)
- [struct MTRColorControlColorCapabilitiesBitmap](mtrcolorcontrolcolorcapabilitiesbitmap.md)
- [struct MTRColorControlOptionsBitmap](mtrcolorcontroloptionsbitmap.md)
- [struct MTRColorControlUpdateFlagsBitmap](mtrcolorcontrolupdateflagsbitmap.md)
- [struct MTRCommissionerControlSupportedDeviceCategoryBitmap](mtrcommissionercontrolsupporteddevicecategorybitmap.md)
- [struct MTRDeviceEnergyManagementFeature](mtrdeviceenergymanagementfeature.md)
- [struct MTRDishwasherAlarmAlarmBitmap](mtrdishwasheralarmalarmbitmap.md)
- [struct MTRDishwasherAlarmFeature](mtrdishwasheralarmfeature.md)
- [struct MTREnergyEVSEFeature](mtrenergyevsefeature.md)
- [struct MTREnergyEVSETargetDayOfWeekBitmap](mtrenergyevsetargetdayofweekbitmap.md)
- [struct MTRGeneralDiagnosticsFeature](mtrgeneraldiagnosticsfeature.md)
- [struct MTRICDManagementFeature](mtricdmanagementfeature.md)
- [struct MTRICDManagementUserActiveModeTriggerBitmap](mtricdmanagementuseractivemodetriggerbitmap.md)
- [struct MTRLaundryWasherControlsFeature](mtrlaundrywashercontrolsfeature.md)
- [struct MTRMessagesFeature](mtrmessagesfeature.md)
- [struct MTRMessagesMessageControlBitmap](mtrmessagesmessagecontrolbitmap.md)
- [struct MTRMicrowaveOvenControlFeature](mtrmicrowaveovencontrolfeature.md)
- [struct MTRNetworkCommissioningThreadCapabilitiesBitmap](mtrnetworkcommissioningthreadcapabilitiesbitmap.md)
- [struct MTROccupancySensingFeature](mtroccupancysensingfeature.md)
- [struct MTRPowerTopologyFeature](mtrpowertopologyfeature.md)
- [struct MTRRefrigeratorAlarmAlarmBitmap](mtrrefrigeratoralarmalarmbitmap.md)
- [struct MTRServiceAreaFeature](mtrserviceareafeature.md)
- [struct MTRTemperatureControlFeature](mtrtemperaturecontrolfeature.md)
- [struct MTRThermostatACErrorCodeBitmap](mtrthermostatacerrorcodebitmap.md)
- [struct MTRThermostatHVACSystemTypeBitmap](mtrthermostathvacsystemtypebitmap.md)
- [struct MTRThermostatOccupancyBitmap](mtrthermostatoccupancybitmap.md)
- [struct MTRThermostatPresetTypeFeaturesBitmap](mtrthermostatpresettypefeaturesbitmap.md)
- [struct MTRThermostatProgrammingOperationModeBitmap](mtrthermostatprogrammingoperationmodebitmap.md)
- [struct MTRThermostatRelayStateBitmap](mtrthermostatrelaystatebitmap.md)
- [struct MTRThermostatRemoteSensingBitmap](mtrthermostatremotesensingbitmap.md)
- [struct MTRThermostatScheduleTypeFeaturesBitmap](mtrthermostatscheduletypefeaturesbitmap.md)
- [struct MTRThreadBorderRouterManagementFeature](mtrthreadborderroutermanagementfeature.md)
- [struct MTRTimeSynchronizationFeature](mtrtimesynchronizationfeature.md)
- [struct MTRWaterHeaterManagementFeature](mtrwaterheatermanagementfeature.md)
- [struct MTRWaterHeaterManagementWaterHeaterHeatSourceBitmap](mtrwaterheatermanagementwaterheaterheatsourcebitmap.md)
### Variables
- [let MTRDeviceControllerRegistrationControllerCompressedFabricIDKey: String](mtrdevicecontrollerregistrationcontrollercompressedfabricidkey.md)
- [let MTRDeviceControllerRegistrationControllerContextKey: String](mtrdevicecontrollerregistrationcontrollercontextkey.md)
- [let MTRDeviceControllerRegistrationControllerIsRunningKey: String](mtrdevicecontrollerregistrationcontrollerisrunningkey.md)
- [let MTRDeviceControllerRegistrationControllerNodeIDKey: String](mtrdevicecontrollerregistrationcontrollernodeidkey.md)
- [let MTRDeviceControllerRegistrationDeviceInternalStateKey: String](mtrdevicecontrollerregistrationdeviceinternalstatekey.md)
- [let MTRDeviceControllerRegistrationNodeIDKey: String](mtrdevicecontrollerregistrationnodeidkey.md)
- [let MTRDeviceControllerRegistrationNodeIDsKey: String](mtrdevicecontrollerregistrationnodeidskey.md)
### Functions
- [func MTREventNameForID(MTRClusterIDType, MTREventIDType) -> String!](mtreventnameforid(_:_:).md)
  Resolve Matter event IDs into a descriptive string.
- [func MTRRequestCommandNameForID(MTRClusterIDType, MTRCommandIDType) -> String!](mtrrequestcommandnameforid(_:_:).md)
  Resolve Matter request (client to server) command IDs into a descriptive string.
- [func MTRResponseCommandNameForID(MTRClusterIDType, MTRCommandIDType) -> String!](mtrresponsecommandnameforid(_:_:).md)
  Resolve Matter response (server to client) command IDs into a descriptive string.
### Enumerations
- [enum MTRAccessControlAccessRestrictionType](mtraccesscontrolaccessrestrictiontype.md)
- [enum MTRChannelType](mtrchanneltype.md)
- [enum MTRColorControlDirection](mtrcolorcontroldirection.md)
- [enum MTRColorControlDriftCompensation](mtrcolorcontroldriftcompensation.md)
- [enum MTRColorControlEnhancedColorMode](mtrcolorcontrolenhancedcolormode.md)
- [enum MTRColorControlMoveMode](mtrcolorcontrolmovemode.md)
- [enum MTRColorControlStepMode](mtrcolorcontrolstepmode.md)
- [enum MTRContentAppObserverStatus](mtrcontentappobserverstatus.md)
- [enum MTRDataTypeAtomicRequestTypeEnum](mtrdatatypeatomicrequesttypeenum.md)
- [enum MTRDataTypeLandmarkTag](mtrdatatypelandmarktag.md)
- [enum MTRDataTypePositionTag](mtrdatatypepositiontag.md)
- [enum MTRDataTypeRelativePositionTag](mtrdatatyperelativepositiontag.md)
- [enum MTRDeviceEnergyManagementAdjustmentCause](mtrdeviceenergymanagementadjustmentcause.md)
- [enum MTRDeviceEnergyManagementCause](mtrdeviceenergymanagementcause.md)
- [enum MTRDeviceEnergyManagementCostType](mtrdeviceenergymanagementcosttype.md)
- [enum MTRDeviceEnergyManagementESAState](mtrdeviceenergymanagementesastate.md)
- [enum MTRDeviceEnergyManagementESAType](mtrdeviceenergymanagementesatype.md)
- [enum MTRDeviceEnergyManagementForecastUpdateReason](mtrdeviceenergymanagementforecastupdatereason.md)
- [enum MTRDeviceEnergyManagementModeModeTag](mtrdeviceenergymanagementmodemodetag.md)
- [enum MTRDeviceEnergyManagementOptOutState](mtrdeviceenergymanagementoptoutstate.md)
- [enum MTRDeviceEnergyManagementPowerAdjustReason](mtrdeviceenergymanagementpoweradjustreason.md)
- [enum MTRDeviceTypeIDType](mtrdevicetypeidtype.md)
- [enum MTRDishwasherModeModeTag](mtrdishwashermodemodetag.md)
- [enum MTRElectricalEnergyMeasurementMeasurementType](mtrelectricalenergymeasurementmeasurementtype.md)
- [enum MTREnergyEVSEEnergyTransferStoppedReason](mtrenergyevseenergytransferstoppedreason.md)
- [enum MTREnergyEVSEFaultState](mtrenergyevsefaultstate.md)
- [enum MTREnergyEVSEModeModeTag](mtrenergyevsemodemodetag.md)
- [enum MTREnergyEVSEState](mtrenergyevsestate.md)
- [enum MTREnergyEVSESupplyState](mtrenergyevsesupplystate.md)
- [enum MTRICDManagementClientType](mtricdmanagementclienttype.md)
- [enum MTRICDManagementOperatingMode](mtricdmanagementoperatingmode.md)
- [enum MTRLaundryDryerControlsDrynessLevel](mtrlaundrydryercontrolsdrynesslevel.md)
- [enum MTRLaundryWasherControlsNumberOfRinses](mtrlaundrywashercontrolsnumberofrinses.md)
- [enum MTRLaundryWasherModeModeTag](mtrlaundrywashermodemodetag.md)
- [enum MTRMediaPlaybackCharacteristic](mtrmediaplaybackcharacteristic.md)
- [enum MTRMessagesFutureMessagePreference](mtrmessagesfuturemessagepreference.md)
- [enum MTRMessagesMessagePriority](mtrmessagesmessagepriority.md)
- [enum MTRMicrowaveOvenModeModeTag](mtrmicrowaveovenmodemodetag.md)
- [enum MTROvenCavityOperationalStateErrorState](mtrovencavityoperationalstateerrorstate.md)
- [enum MTROvenCavityOperationalStateOperationalState](mtrovencavityoperationalstateoperationalstate.md)
- [enum MTROvenModeModeTag](mtrovenmodemodetag.md)
- [enum MTRRefrigeratorAndTemperatureControlledCabinetModeModeTag](mtrrefrigeratorandtemperaturecontrolledcabinetmodemodetag.md)
- [enum MTRServiceAreaOperationalStatus](mtrserviceareaoperationalstatus.md)
- [enum MTRServiceAreaSelectAreasStatus](mtrserviceareaselectareasstatus.md)
- [enum MTRServiceAreaSkipAreaStatus](mtrserviceareaskipareastatus.md)
- [enum MTRThermostatACCapacityFormat](mtrthermostataccapacityformat.md)
- [enum MTRThermostatACCompressorType](mtrthermostataccompressortype.md)
- [enum MTRThermostatACLouverPosition](mtrthermostataclouverposition.md)
- [enum MTRThermostatACRefrigerantType](mtrthermostatacrefrigeranttype.md)
- [enum MTRThermostatACType](mtrthermostatactype.md)
- [enum MTRThermostatPresetScenario](mtrthermostatpresetscenario.md)
- [enum MTRThermostatSetpointChangeSource](mtrthermostatsetpointchangesource.md)
- [enum MTRThermostatStartOfWeek](mtrthermostatstartofweek.md)
- [enum MTRThermostatTemperatureSetpointHold](mtrthermostattemperaturesetpointhold.md)
- [enum MTRTimeSynchronizationStatusCode](mtrtimesynchronizationstatuscode.md)
- [enum MTRTimeSynchronizationTimeZoneDatabase](mtrtimesynchronizationtimezonedatabase.md)
- [enum MTRWaterHeaterManagementBoostState](mtrwaterheatermanagementbooststate.md)
- [enum MTRWaterHeaterModeModeTag](mtrwaterheatermodemodetag.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Matter)*